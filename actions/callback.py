from bot_config import bot, chat_name
from keyboards import inline_menu_ElectricTrain_Yes, inline_menu_ElectricTrain_No, inline_menu_ElectricTrain_main
from actions.get_ElectricTrain import Streshnevo_Istra, Istra_Streshnevo, Istra_Dmitrovskaya, Istra_Tushino, Dmitrovskaya_Istra, Tushino_Istra

def functions():
    @bot.callback_query_handler(func=lambda call: True)
    def func(call):
        if call.data == 'YES':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери направление', reply_markup=inline_menu_ElectricTrain_Yes)
        elif call.data == 'NO':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери направление', reply_markup=inline_menu_ElectricTrain_No)
        elif call.data == 'Streshnevo_Istra_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Streshnevo_Istra(True))
        elif call.data == 'Istra_Streshnevo_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Streshnevo(True))
        elif call.data == 'Dmitrovskaya_Istra_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Dmitrovskaya_Istra(True))
        elif call.data == 'Istra_Dmitrovskaya_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Dmitrovskaya(True))
        elif call.data == 'Tushino_Istra_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Tushino_Istra(True))
        elif call.data == 'Istra_Tushino_Yes': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Tushino(True))
        elif call.data == 'Streshnevo_Istra_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Streshnevo_Istra())
        elif call.data == 'Istra_Streshnevo_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Streshnevo())
        elif call.data == 'Dmitrovskaya_Istra_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Dmitrovskaya_Istra())
        elif call.data == 'Istra_Dmitrovskaya_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Dmitrovskaya())
        elif call.data == 'Tushino_Istra_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Tushino_Istra())
        elif call.data == 'Istra_Tushino_No': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Tushino())
        elif call.data == 'Back': 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вывести расписание полностью?', reply_markup=inline_menu_ElectricTrain_main)