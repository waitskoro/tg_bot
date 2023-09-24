import telebot
from telebot import types
import random

bot = telebot.TeleBot('Your_token')

file1 = open("sample.txt", encoding='utf-8')
lines = file1.readlines()
file1.close()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Прислать любовь ❤️"))
    bot.send_message(message.chat.id, "Добро пожаловать!\nДанный бот создан для тебя", reply_markup=keyboard)

@bot.message_handler(commands=['get_love'])
def get_love(message):
    random_line = random.choice(lines)
    bot.send_message(message.chat.id, random_line)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Прислать любовь ❤️":
        get_love(message)

# Запускаем бота
bot.polling(none_stop=True)
