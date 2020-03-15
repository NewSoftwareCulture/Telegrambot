from bot_config import bot, chat_name
from keyboards import menu_main, inline_menu_chat, inline_menu_channel, menu_main_bot

def functions():
    @bot.message_handler(
        commands=['start'], 
    )
    def func_start(message):
        bot.send_message(message.chat.id, 'Лучше бы я пошел с мастером Люком, чем торчал здесь с тобой. Уж не знаю в чём дело, но уверен, что в этом есть твоя вина!')
    
    @bot.message_handler(
        commands=['help'], 
    )
    def func_help(message):
        bot.send_message(message.chat.id, 'Ooops! Кажется, кто-то потерялся. Чтобы узнать, что я могу, введи "/menu". До встречи!')

    @bot.message_handler(
        commands=['menu'], 
    )
    def func_menu(message):
        if message.chat.id > 0:
            bot.send_message(message.chat.id, '1 sec', reply_markup=menu_main_bot)
        else:
            bot.send_message(message.chat.id, '1 sec', reply_markup=menu_main)
    
    @bot.message_handler(
        commands=['anon'], 
    )
    def func_anon(message):
        if message.chat.id > 0:
            message.text = message.text.replace('/anon ', '')
            bot.send_message(chat_name, message.text)

    @bot.message_handler(
        commands=['chat'], 
    )
    def func_add(message):
        if message.chat.id > 0:
            bot.send_message(message.chat.id, 'Чтобы перейти в чат нажми ⬇️', reply_markup=inline_menu_chat)

    @bot.message_handler(
        commands=['channel'], 
    )
    def func_add(message):
        if message.chat.id > 0:
            bot.send_message(message.chat.id, 'Чтобы перейти в канал нажми ⬇️', reply_markup=inline_menu_channel)