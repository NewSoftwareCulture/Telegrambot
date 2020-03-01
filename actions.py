from bot_config import bot

def commands():
    @bot.message_handler(
        commands=['start'], 
    )
    def func(message):
        bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')


def messages():
    @bot.message_handler(
        content_types=['text'],
    )
    def func(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + ", я тут местный бот")
        if message.text.lower().find('id'):
            bot.send_message(message.chat.id, "Твой ID: " + message.chat.id)
        if message.text.lower().find('ip') > -1:
            bot.send_message(message.chat.id, "Твой IP: " + message.from_user.ip)