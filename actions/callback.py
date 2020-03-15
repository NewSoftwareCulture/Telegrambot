from bot_config import bot, chat_name
from keyboards import inline_menu_ElectricTrain_main, inline_menu_ElectricTrain
from actions.get_ElectricTrain import Streshnevo_Istra, Istra_Streshnevo, Istra_Dmitrovskaya, Istra_Tushino, Dmitrovskaya_Istra, Tushino_Istra

def functions():
    @bot.callback_query_handler(func=lambda call: True)
    def func(call):
        if call.data == 'YES':
            inline_menu_ElectricTrain.status = True
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери направление', reply_markup=inline_menu_ElectricTrain)
        elif call.data == 'NO':
            inline_menu_ElectricTrain.status = False
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери направление', reply_markup=inline_menu_ElectricTrain)
        elif call.data == 'Streshnevo_Istra': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Streshnevo_Istra(inline_menu_ElectricTrain.status))
        elif call.data == 'Istra_Streshnevo': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Streshnevo(inline_menu_ElectricTrain.status))
        elif call.data == 'Dmitrovskaya_Istra': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Dmitrovskaya_Istra(inline_menu_ElectricTrain.status))
        elif call.data == 'Istra_Dmitrovskaya': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Dmitrovskaya(inline_menu_ElectricTrain.status))
        elif call.data == 'Tushino_Istra': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Tushino_Istra(inline_menu_ElectricTrain.status))
        elif call.data == 'Istra_Tushino': 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Лови ✨✨✨✨')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Istra_Tushino(inline_menu_ElectricTrain.status))
        elif call.data == 'Back': 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вывести расписание полностью?', reply_markup=inline_menu_ElectricTrain_main)