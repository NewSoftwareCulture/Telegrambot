import telebot
import requests
import time
import config

bot = telebot.TeleBot(config.token)


while True:
    try:
        @bot.message_handler(commands=['hi','hello',"Hi","Hello"])
        def start_message(message):
            bot.send_message(message.chat.id, 'Здарова, я твой бот, бро')

        @bot.message_handler(commands=['action'])
        def message1(message):
            bot.send_message(message.chat.id, 'Да я многое могу')

        @bot.message_handler(commands=['finish'])
        def message2(message):
            bot.send_message(message.chat.id, 'Пока, чел')

        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
    