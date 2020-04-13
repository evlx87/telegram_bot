"""Простой телеграм бот"""
import json
import telebot
from telebot import apihelper

# Получаем данные настроек из JSON файла config.json
with open('config.json', 'r', encoding='utf-8') as f:
    bot_api = json.load(f)

# Подключаем бота с полученными настройками
bot = telebot.TeleBot(bot_api['token'])
apihelper.proxy = {'https': bot_api['proxy_url']}


@bot.message_handler(commands=['start'])
def start_message(message):
    """Сообщение приветствия"""
    bot.send_message(message.chat.id, 'Привет, землянин!'
                                      '\nМеня зовут TestBot и буду рад помочь тебе.'
                                      '\nНапиши /help чтобы узнать что я умею')


@bot.message_handler(content_types=['text'])
def help_message(message):
    """Функция диалога с пользователем по различным сценариям в зависимости"""
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling()
