from bot_config import bot

def start_mes():
    @bot.message_handler(
        commands=['start'], 
    )
    def start_command(message):
        bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')


def message_usr():
    @bot.message_handler(
        content_types=['text'],
    )
    def messages(message):
        if message.text.lower() == 'hi':
            bot.send_message(message.chat.id, 'Здарова, я твой бот, бро')
        elif message.text.lower() == 'action':
            bot.send_message(message.chat.id, 'Да я многое могу')
        elif message.text.lower() == 'finish':
            bot.send_message(message.chat.id, 'Пока, чел')  