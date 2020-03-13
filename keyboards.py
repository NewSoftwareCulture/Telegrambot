import telebot

menu_main = telebot.types.ReplyKeyboardMarkup(True, False)
menu_main.row('ID', 'Погода 🌍', '123')
menu_main.row('Электрички 🚇', 'МЦК 🚇')

menu_weather = telebot.types.ReplyKeyboardMarkup(True, False)
menu_weather.row('Москва 🌍', 'Истра 🌍')
menu_weather.row('Тольятти 🌍', 'Питер 🌍')

menu_MoskowCentralRing = telebot.types.ReplyKeyboardMarkup(True, False)
menu_MoskowCentralRing.row('Лужники 🚇', 'Деловой центр 🚇')

menu_ElectrincTrain = telebot.types.ReplyKeyboardMarkup(True, False)
menu_ElectrincTrain.row('На Истру 🚇', 'На Москву 🚇')