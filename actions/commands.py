from bot_config import bot
from bot_config import chat_name
from keyboards import menu_main
from keyboards import menu_Aliance

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
        bot.send_message(message.chat.id, '1 sec', reply_markup=menu_main)

    @bot.message_handler(
        commands=['anon'], 
    )
    def func_anon(message):
        if message.chat.id > 0:
            message.text = message.text.replace('/anon ', '')
            bot.send_message(chat_name, message.text)
            bot.send_photo(chat_name, message)
            bot.send_poll(chat_name, message)