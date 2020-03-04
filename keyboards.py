import telebot

menu_main = telebot.types.ReplyKeyboardMarkup(True, False)
menu_main.row('ID', 'Погода', 'Aliance', 'Horge')

menu_Aliance = telebot.types.ReplyKeyboardMarkup(True, False)
menu_Aliance.row('Human', 'Dwarf','Gnome', 'Night Elf','Drenei')

menu_Horge = telebot.types.ReplyKeyboardMarkup(True, False)
menu_Horge.row('Ork', 'Blood Elf', 'Troll', 'Tauren', 'Undead')