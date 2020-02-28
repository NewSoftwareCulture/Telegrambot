import telebot
import requests
import time
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я твой бот, привет')
# def start_message(message):
    # bot.send_message(message.chat.id, 'Я твой бот, привет')
bot.polling()