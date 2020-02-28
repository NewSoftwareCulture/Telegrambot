import telebot
# import config
from main import bot


def message1(message):
    bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')
            
def message2(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Здарова, я твой бот, бро')
    elif message.text.lower() == 'action':
        bot.send_message(message.chat.id, 'Да я многое могу')
    elif message.text.lower() == 'finish':
        bot.send_message(message.chat.id, 'Пока, чел')
    # elif message.text.lower() == 'channel':
    #     bot.send_message(config.channel_name, 'Пишу в канал')
    # elif message.text.lower() == 'chat':
    #     bot.send_message(config.chat_name, 'Пишу в чат') 