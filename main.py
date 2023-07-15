from telebot import TeleBot, types
from dotenv import load_dotenv
load_dotenv()
from os import getenv
from json import load

TgBot = TeleBot(getenv("TOKEN"))

def jsonloader(jsonFile="data.json"):
    with open(jsonFile, "r") as jsonFile:
        return load(jsonFile)

@TgBot.message_handler(commands=jsonloader()["commands"])
def command_handler(msg):
    for command in jsonloader()["commands"]:
        if (msg.text==command):
            try:
                TgBot.send_message(msg, jsonloader()["func"][msg.text])
            except Exception as e:
                print(e)

TgBot.infinity_polling()
