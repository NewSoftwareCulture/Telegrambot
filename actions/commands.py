from bot_config import bot
from bot_config import chat_name

def functions():
    @bot.message_handler(
        commands=['start'], 
    )
    def func_start(message):
        bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')
    
    @bot.message_handler(
        commands=['menu'], 
    )
    def func_menu(message):
        bot.send_message(message.chat.id, "Напиши 'ID' для получения своего id\nМожешь написать 'привет' и я поздороваюсь с тобой")

    @bot.message_handler(
        commands=['anon'], 
    )
    def func_menu(message):
        if message.chat.id > 0:
            message.text = message.text.replace('/anon ', '')
            bot.send_message(chat_name, message.text)