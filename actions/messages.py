from bot_config import bot
from actions.get_weather import moskow, spb, istra, tlt
from actions.get_MoskowCentralRing import Lushniki, DelovoyCenter
import keyboards

def functions():
    @bot.message_handler(
        content_types=['text'],
    )
    def func(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, "Привет, @" + message.from_user.username + ", я тут местный бот")
        elif message.text.lower().find('id') > -1:
            bot.send_message(message.chat.id, "Твой ID: " + str(message.from_user.id))
        
        elif message.text.lower() == 'погода 🌍':
            bot.send_message(message.chat.id, 'Выбери город', reply_markup=keyboards.menu_weather)
        elif message.text == 'Москва 🌍':
            if message.chat.id > 0: bot.send_message(message.chat.id, moskow(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, moskow(), reply_markup=keyboards.menu_main)
        elif message.text == 'Истра 🌍':
            if message.chat.id > 0: bot.send_message(message.chat.id, istra(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, istra(), reply_markup=keyboards.menu_main)
        elif message.text == 'Тольятти 🌍':
            if message.chat.id > 0: bot.send_message(message.chat.id, tlt(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, tlt(), reply_markup=keyboards.menu_main)
        elif message.text == 'Питер 🌍':
            if message.chat.id > 0: bot.send_message(message.chat.id, spb(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, spb(), reply_markup=keyboards.menu_main)

        elif message.text == 'Электрички 🚇':
            bot.send_message(message.chat.id, 'Вывести расписание полностью?', reply_markup=keyboards.inline_menu_ElectricTrain_main)
        elif message.text == 'МЦК 🚇':
            bot.send_message(message.chat.id, 'Выбери направление', reply_markup=keyboards.menu_MoskowCentralRing)
        elif message.text == 'Лужники 🚇':
            if message.chat.id > 0: bot.send_message(message.chat.id, Lushniki(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, Lushniki(), reply_markup=keyboards.menu_main)
        elif message.text == 'Деловой центр 🚇':
            if message.chat.id > 0: bot.send_message(message.chat.id, DelovoyCenter(), reply_markup=keyboards.menu_main_bot)
            else: bot.send_message(message.chat.id, DelovoyCenter(), reply_markup=keyboards.menu_main)    