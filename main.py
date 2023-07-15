from telebot import TeleBot, types
from dotenv import load_dotenv
load_dotenv()
from os import getenv
from json import load
from re import findall

TgBot = TeleBot(getenv("TOKEN"))
btnReg = r"~btn\?\w*\?\w*\:\w*\//\w*\.\w*\/\w*"

def jsonloader(jsonFile="data.json"):
    with open(jsonFile, "r") as jsonFile:
        return load(jsonFile)

@TgBot.message_handler(commands=list(jsonloader()["func"].keys()))
def command_handler(msg):
    Keyboard = types.InlineKeyboardMarkup()
    msgtxt = msg.text.replace("/","")
    for command in jsonloader()["func"].keys():
        if (msgtxt==command):
            reply_com = jsonloader()["func"][command]
            findList = findall(btnReg, reply_com)
            if (len(findList)):
                for btn in findList:
                    btnData = btn.split("?")
                    Keyboard.add(types.InlineKeyboardButton(text=btnData[1], url=btnData[2]))
                    reply_fin = reply_com.replace("".join(findList),"")
            try:
                TgBot.send_message(msg.chat.id, reply_fin, reply_markup=Keyboard)
            except Exception as e:
                print(e)

TgBot.infinity_polling()
