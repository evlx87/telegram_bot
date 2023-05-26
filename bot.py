import json
import telebot
from telebot import apihelper

# Загрузка конфигурации из файла JSON
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        bot_api = json.load(f)
except FileNotFoundError:
    print('Файл конфигурации не найден')
    exit()
except json.JSONDecodeError:
    print('Неверный файл конфигурации')
    exit()

# Подключение бота с использованием конфигурации
bot = telebot.TeleBot(bot_api['token'])
apihelper.proxy = {'https': bot_api['proxy_url']}

# Сообщение об ошибке
with open('error_messages.json', 'r', encoding='utf-8') as f:
    error_messages = json.load(f)


# Отправка приветственного сообщения
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, землянин!'
                     '\nМеня зовут TestBot и буду рад помочь тебе.'
                     '\nНапиши /help чтобы узнать что я умею')


# Обработка пользовательского ввода
@bot.message_handler(content_types=['text'])
def help_message(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, error_messages['unknown_command'])
    else:
        bot.send_message(message.from_user.id, error_messages['unknown_input'])


# Запуск бота
bot.polling()
