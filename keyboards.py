import telebot
from telebot import types
from bot_config import chat_id, channel_id

menu_main = telebot.types.ReplyKeyboardMarkup(True, False)
menu_main.row('ID', 'Погода 🌍')
menu_main.row('Электрички 🚇', 'МЦК 🚇')

menu_main_bot = telebot.types.ReplyKeyboardMarkup(True, False)
menu_main_bot.row('ID', 'Погода 🌍')
menu_main_bot.row('Электрички 🚇', 'МЦК 🚇')
menu_main_bot.row('/chat', '/channel')

menu_weather = telebot.types.ReplyKeyboardMarkup(True, False)
menu_weather.row('Москва 🌍', 'Истра 🌍')
menu_weather.row('Тольятти 🌍', 'Питер 🌍')

menu_MoskowCentralRing = telebot.types.ReplyKeyboardMarkup(True, False)
menu_MoskowCentralRing.row('Лужники 🚇', 'Деловой центр 🚇')

inline_menu_chat = types.InlineKeyboardMarkup(row_width=1)
chat_button = types.InlineKeyboardButton(text='✨ Кнопочка ✨', url=chat_id)
inline_menu_chat.add(chat_button)

inline_menu_channel = types.InlineKeyboardMarkup(row_width=1)
channel_button = types.InlineKeyboardButton(text='✨ Кнопочка ✨', url=channel_id)
inline_menu_channel.add(channel_button)

inline_menu_ElectricTrain_main = types.InlineKeyboardMarkup(row_width=2)
button_Yes = types.InlineKeyboardButton(text='Yes', callback_data='YES')
button_No = types.InlineKeyboardButton(text='No', callback_data='NO')
inline_menu_ElectricTrain_main.add(button_No, button_Yes)


# Переделать это говно в прототип types.InlineKeyboardMarkup с дополнительным параметром status 
# class my_Keyboard(types.InlineKeyboardMarkup):
#     def __init__(self, row_width=3, status):
#         self.row_width = row_width
#         self.keyboard = []
#         self.status_ = status

inline_menu_ElectricTrain_Yes = types.InlineKeyboardMarkup(row_width=3)
ElectricTrain_button_1_Yes = types.InlineKeyboardButton(text='Истра', callback_data='Streshnevo_Istra_Yes')
ElectricTrain_button_2_Yes = types.InlineKeyboardButton(text='Стрешнево', callback_data='Istra_Streshnevo_Yes')
ElectricTrain_button_3_Yes = types.InlineKeyboardButton(text='Истра', callback_data='Dmitrovskaya_Istra_Yes')
ElectricTrain_button_4_Yes = types.InlineKeyboardButton(text='Дмитровская', callback_data='Istra_Dmitrovskaya_Yes')
ElectricTrain_button_5_Yes = types.InlineKeyboardButton(text='Истра', callback_data='Tushino_Istra_Yes')
ElectricTrain_button_6_Yes = types.InlineKeyboardButton(text='Тушино', callback_data='Istra_Tushino_Yes')
ElectricTrain_button_7 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
inline_menu_ElectricTrain_Yes.add(ElectricTrain_button_1_Yes, ElectricTrain_button_2_Yes)
inline_menu_ElectricTrain_Yes.add(ElectricTrain_button_3_Yes, ElectricTrain_button_4_Yes)
inline_menu_ElectricTrain_Yes.add(ElectricTrain_button_5_Yes, ElectricTrain_button_6_Yes)
inline_menu_ElectricTrain_Yes.add(ElectricTrain_button_7)

inline_menu_ElectricTrain_No = types.InlineKeyboardMarkup(row_width=3)
ElectricTrain_button_1_No = types.InlineKeyboardButton(text='Истра', callback_data='Streshnevo_Istra_No')
ElectricTrain_button_2_No = types.InlineKeyboardButton(text='Стрешнево', callback_data='Istra_Streshnevo_No')
ElectricTrain_button_3_No = types.InlineKeyboardButton(text='Истра', callback_data='Dmitrovskaya_Istra_No')
ElectricTrain_button_4_No = types.InlineKeyboardButton(text='Дмитровская', callback_data='Istra_Dmitrovskaya_No')
ElectricTrain_button_5_No = types.InlineKeyboardButton(text='Истра', callback_data='Tushino_Istra_No')
ElectricTrain_button_6_No = types.InlineKeyboardButton(text='Тушино', callback_data='Istra_Tushino_No')
inline_menu_ElectricTrain_No.add(ElectricTrain_button_1_No, ElectricTrain_button_2_No)
inline_menu_ElectricTrain_No.add(ElectricTrain_button_3_No, ElectricTrain_button_4_No)
inline_menu_ElectricTrain_No.add(ElectricTrain_button_5_No, ElectricTrain_button_6_No)
inline_menu_ElectricTrain_No.add(ElectricTrain_button_7)