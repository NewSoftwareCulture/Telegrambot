import telebot
import requests
import time
import config
import actions

bot = telebot.TeleBot(config.token)
       
while True:
    try:
        @bot.message_handler(commands=['start'])
        def start_command(message):
            bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')
     
        @bot.message_handler(content_types=['text'])
        def messages(message):
            if message.text.lower() == 'hi':
                bot.send_message(message.chat.id, 'Здарова, я твой бот, бро')
            elif message.text.lower() == 'action':
                bot.send_message(message.chat.id, 'Да я многое могу')
            elif message.text.lower() == 'finish':
                bot.send_message(message.chat.id, 'Пока, чел')  
        bot.polling(none_stop=True)

    except Exception as e:
        # print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(1)
    