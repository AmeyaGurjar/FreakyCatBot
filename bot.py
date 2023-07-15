import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Start command
@bot.message_handler(commands=['start'])
def send_start(message):
    start_msg = "Hi! I'm Freaky's Redirect Bot"
    bot.reply_to(message, start_msg)

    start_btn = types.KeyboardButton("Open Menu")
    start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_markup.add(start_btn)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=start_markup)

# Menu keyboard
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row("/start", "/help")
menu_keyboard.row("/channel", "/group")
menu_keyboard.row("/ot", "/donate", "/owner")
menu_keyboard.row("/veux", "/peux", "/walls")

# Help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Use the menu to navigate me!"
    bot.reply_to(message, help_text, reply_markup=menu_keyboard)

# Channel command
@bot.message_handler(commands=['channel'])
def send_channel(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://t.me/example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "My Channel", reply_markup=markup)

# Add other command handlers - group, ot, donate, owner, walls

# Group command
@bot.message_handler(commands=['group'])
def send_Group(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://t.me/example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "My Group", reply_markup=markup)

# OT Channel command
@bot.message_handler(commands=['ot'])
def send_ot(message):
    channel_btn = types.InlineKeyboardButton("Group", url="https://t.me/example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "OFF-Topic", reply_markup=markup)


# Donate command
@bot.message_handler(commands=['donate'])
def send_donate(message):
    channel_btn = types.InlineKeyboardButton("Donate", url="https://t.me/example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "If You Like My Work:)", reply_markup=markup)

# Owner command
@bot.message_handler(commands=['owner'])
def send_owner(message):
    channel_btn = types.InlineKeyboardButton("Profile", url="https:/example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "My Master", reply_markup=markup)

# Walls command
@bot.message_handler(commands=['walls'])
def send_walls(message):
    channel_btn = types.InlineKeyboardButton("Here.", url="https://example")
    markup = types.InlineKeyboardMarkup()
    markup.add(channel_btn)
    bot.reply_to(message, "Best Wallpapers", reply_markup=markup)

# Veux/Peux commands
@bot.message_handler(commands=['veux', 'peux'])
def send_links(message):
    button1 = types.InlineKeyboardButton("Channel", url="https://t.me/pocox4proupdates")
    button2 = types.InlineKeyboardButton("Group", url="https://t.me/pocox4proofficial")
    button3 = types.InlineKeyboardButton("Archive", url="https://t.me/VeuxRoms")

    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)

    bot.reply_to(message, "Veux|Peux", reply_markup=markup)

# Default handler
@bot.message_handler(func=lambda message: True)
def default_command(message):
    bot.reply_to(message, "Choose an option:", reply_markup=menu_keyboard)

bot.polling()
