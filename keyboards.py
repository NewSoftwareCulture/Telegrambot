import telebot

menu_main = telebot.types.ReplyKeyboardMarkup(True, False)
menu_main.row('ID', 'Погода', 'Aliance', 'Horge')

menu_weather = telebot.types.ReplyKeyboardMarkup(False, True)
menu_weather.row('Москва 🌍', 'Истра 🌍')
menu_weather.row('Тольятти 🌍', 'Питер 🌍')

menu_Aliance = telebot.types.ReplyKeyboardMarkup(False, False)
menu_Aliance.row('Human', 'Dwarf')
menu_Aliance.row('Gnome', 'Drenei')
menu_Aliance.row('Night Elf')

menu_Horge = telebot.types.ReplyKeyboardMarkup(False, True)
menu_Horge.row('Ork', 'Troll')
menu_Horge.row('Tauren', 'Undead')
menu_Horge.row('Blood Elf')