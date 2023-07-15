from telebot import TeleBot, types
from dotenv import load_dotenv
load_dotenv()
from os import getenv
from json import load

TgBot = TeleBot(getenv("TOKEN"))

def jsonloader(jsonFile="data.json"):
    with open(jsonFile, "r") as jsonFile:
        return load(jsonFile)

@TgBot.message_handler(commands=jsonloader()["func"].keys())
def command_handler(msg):
    msgtxt = msg.text.replace("/","")
    for command in jsonloader()["func"].keys():
        if (msgtxt==command):
            try:
                TgBot.send_message(msg, jsonloader()["func"][msgtxt])
            except Exception as e:
                print(e)

TgBot.infinity_polling()
