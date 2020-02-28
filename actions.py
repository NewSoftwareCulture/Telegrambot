import telebot
from main import bot


@bot.message_handler(commands=['hi','hello',"Hi","Hello"])
def start_message(message):
    bot.send_message(message.chat.id, 'Здарова, я твой бот, бро')
@bot.message_handler(commands=['action'])
def message1(message):
    bot.send_message(message.chat.id, 'Да я многое могу')
@bot.message_handler(commands=['finish'])
def message2(message):
    bot.send_message(message.chat.id, 'Пока, чел')
