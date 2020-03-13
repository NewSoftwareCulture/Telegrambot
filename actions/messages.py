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
            bot.send_message(message.chat.id, moskow(), reply_markup=keyboards.menu_main)
        elif message.text == 'Истра 🌍':
            bot.send_message(message.chat.id, istra(), reply_markup=keyboards.menu_main)
        elif message.text == 'Тольятти 🌍':
            bot.send_message(message.chat.id, tlt(), reply_markup=keyboards.menu_main)
        elif message.text == 'Питер 🌍':
            bot.send_message(message.chat.id, spb(), reply_markup=keyboards.menu_main)

        elif message.text == 'Электрички 🚇':
            bot.send_message(message.chat.id, 'Выбери направление', reply_markup=keyboards.menu_ElectrincTrain)
        elif message.text == 'МЦК 🚇':
            bot.send_message(message.chat.id, 'Выбери направление', reply_markup=keyboards.menu_MoskowCentralRing)
        elif message.text == 'Лужники 🚇':
            bot.send_message(message.chat.id, Lushniki(), reply_markup=keyboards.menu_main)
        elif message.text == 'Деловой центр 🚇':
            bot.send_message(message.chat.id, DelovoyCenter(), reply_markup=keyboards.menu_main)
        # elif message.text == 'На Истру 🚇':
        #     bot.send_message(message.chat.id, tlt(), reply_markup=keyboards.menu_main)
        # elif message.text == 'На Москву 🚇':
        #     bot.send_message(message.chat.id, spb(), reply_markup=keyboards.menu_main)
    