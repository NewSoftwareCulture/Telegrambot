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

menu_ElectrincTrain = telebot.types.ReplyKeyboardMarkup(True, False)
menu_ElectrincTrain.row('На Истру 🚇', 'На Москву 🚇')

inline_menu_chat = types.InlineKeyboardMarkup(row_width=1)
chat_button = types.InlineKeyboardButton(text='✨ Кнопочка ✨', url=chat_id)
inline_menu_chat.add(chat_button)

inline_menu_channel = types.InlineKeyboardMarkup(row_width=1)
channel_button = types.InlineKeyboardButton(text='✨ Кнопочка ✨', url=channel_id)
inline_menu_channel.add(channel_button)