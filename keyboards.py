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

class CustomKeyboard(types.InlineKeyboardMarkup):
    def __init__(self, row_width=3, status=True):
        self.row_width = row_width
        self.status = status
        self.keyboard = []

inline_menu_ElectricTrain = CustomKeyboard(row_width=4)
ElectricTrain_button_1 = types.InlineKeyboardButton(text='Истра', callback_data='Streshnevo_Istra')
ElectricTrain_button_2 = types.InlineKeyboardButton(text='Стрешнево', callback_data='Istra_Streshnevo')
ElectricTrain_button_3 = types.InlineKeyboardButton(text='Истра', callback_data='Dmitrovskaya_Istra')
ElectricTrain_button_4 = types.InlineKeyboardButton(text='Дмитровская', callback_data='Istra_Dmitrovskaya')
ElectricTrain_button_5 = types.InlineKeyboardButton(text='Истра', callback_data='Tushino_Istra')
ElectricTrain_button_6 = types.InlineKeyboardButton(text='Тушино', callback_data='Istra_Tushino')
ElectricTrain_button_7 = types.InlineKeyboardButton(text='Назад', callback_data='Back')
inline_menu_ElectricTrain.add(ElectricTrain_button_1, ElectricTrain_button_2)
inline_menu_ElectricTrain.add(ElectricTrain_button_3, ElectricTrain_button_4)
inline_menu_ElectricTrain.add(ElectricTrain_button_5, ElectricTrain_button_6)
inline_menu_ElectricTrain.add(ElectricTrain_button_7)