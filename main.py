from telebot import TeleBot, types
from dotenv import load_dotenv
load_dotenv()
from os import getenv
from json import load
from re import findall, sub, IGNORECASE

TgBot = TeleBot(getenv("TOKEN"))
BotUserName = str(getenv("USER"))
btnReg = r"~btn\?\w*?(.*?)\?'(.*?)'"
subReg = r"~btn(.*)"
def jsonloader(jsonFile="data.json"):
    with open(jsonFile, "r") as jsonFile:
        return load(jsonFile)

@TgBot.message_handler(commands=list(jsonloader()["func"].keys()))
def command_handler(msg):
    Keyboard = types.InlineKeyboardMarkup()
    msgtxt = msg.text.replace("/","")
    for command in jsonloader()["func"].keys():
        if (msgtxt==command or msgtxt==f"{command}@{TgBot.get_me().username}"):
            reply_com = jsonloader()["func"][command]
            findList = findall(btnReg, reply_com, IGNORECASE)
            if (len(findList)):
                for btn in findList:
                    Keyboard.add(types.InlineKeyboardButton(text=btn[0], url=btn[1]))
                    reply_com = sub(pattern=subReg, repl="", string=reply_com)
            try:
                TgBot.send_message(msg.chat.id, reply_com, reply_markup=Keyboard)
            except Exception as e:
                print(e)

TgBot.infinity_polling()
