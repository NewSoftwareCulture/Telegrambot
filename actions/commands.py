from bot_config import bot

def commands():
    @bot.message_handler(
        commands=['start'], 
    )
    def func(message):
        bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')