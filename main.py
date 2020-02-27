import telebot
import requests
import time
import config

bot = telebot.TeleBot(config.token)


bot.send_message(config.channel_name, 'hello')

bot.polling()