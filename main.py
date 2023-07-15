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



# Start command
@TgBot.message_handler(commands=['start'])
def send_start(message):
    start_msg = "Hi! I'm Freaky's Redirect Bot"
    TgBot.reply_to(message, start_msg)

    start_btn = types.KeyboardButton("Open Menu")
    start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_markup.add(start_btn)
    TgBot.send_message(message.chat.id, "Choose an option:", reply_markup=start_markup)

# Menu keyboard
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row("/start", "/help")
menu_keyboard.row("/channel", "/group")
menu_keyboard.row("/ot", "/donate", "/owner")
menu_keyboard.row("/veux", "/peux", "/walls")

# Help command
@TgBot.message_handler(commands=['help'])
def send_help(message):
    TgBot.reply_to(message, jsonloader()["help_msg"], reply_markup=menu_keyboard)

# Channel command
@TgBot.message_handler(commands=['channel'])
def send_channel(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://t.me/FreakyCatDumps")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBog.reply_to(message, "My Channel", reply_markup=markup)

# Add other command handlers - group, ot, donate, owner, walls

# Group command
@TgBot.message_handler(commands=['group'])
def send_Group(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://t.me/FreakyCatBuilds")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBot.reply_to(message, "My Group", reply_markup=markup)

# OT Channel command
@TgBot.message_handler(commands=['ot'])
def send_ot(message):
    channel_btn = types.InlineKeyboardButton("Group", url="https://t.me/UnderWorldShit")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBot.reply_to(message, "OFF-Topic", reply_markup=markup)


# Donate command
@TgBot.message_handler(commands=['donate'])
def send_donate(message):
    channel_btn = types.InlineKeyboardButton("Donate", url="https://t.me/FreakyCatDumps/42")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBot.reply_to(message, "If You Like My Work:)", reply_markup=markup)

# Owner command
@TgBot.message_handler(commands=['owner'])
def send_owner(message):
    channel_btn = types.InlineKeyboardButton("Profile", url="https://t.me/MrFreakSins")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBot.reply_to(message, "My Master", reply_markup=markup)

# Walls command
@TgBot.message_handler(commands=['walls'])
def send_walls(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://t.me/FreakyOnFire")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    TgBot.reply_to(message, "Best Wallpapers", reply_markup=markup)

# Veux/Peux commands
@TgBot.message_handler(commands=['veux', 'peux'])
def send_links(message):
    button1 = types.InlineKeyboardButton("Channel", url="https://t.me/pocox4proupdates")
    button2 = types.InlineKeyboardButton("Group", url="https://t.me/pocox4proofficial")
    button3 = types.InlineKeyboardButton("Archive", url="https://t.me/VeuxRoms")

    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)

    TgBot.reply_to(message, "Veux|Peux", reply_markup=markup)

# Default handler only responds to commands
@TgBot.message_handler(func=lambda message: message.text.startswith("/"))
def default_command(message):
    TgBot.reply_to(message, "Choose an option:", reply_markup=menu_keyboard)

# Ignore all other messages
@TgBot.message_handler(func=lambda message: True)
def ignore_other(message):
    pass

# Log channel
log_channel_id = 1226959801

# Existing handlers...

@TgBot.message_handler(func=lambda msg: True)
def log_and_process(msg):

  # Extract info
  chat_id = msg.chat.id
  date = msg.date
  username = msg.from_user.username

  # Log message
  log_text = f"From: {chat_id}\nUsername: @{username}\nDate: {date}\n{msg.text}"
  TgBot.send_message(log_channel_id, log_text)

  # Process message
  default_command(msg)

# Error handling
def send_log(text):
  try:
    TgBot.send_message(log_channel_id, text)
  except Exception as e:
    print('Error sending log:', e)

# Rest of handlers...

TgBot.infinity_polling()
