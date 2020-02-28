import telebot
import requests
import time
import config
import actions

bot = telebot.TeleBot(config.token)


while True:
    try:
        @bot.message_handler(commands=['start'])
            
        @bot.message_handler(content_types=['text'])
        
            
        bot.polling(none_stop=True)

    except Exception as e:
        # print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(1)
    