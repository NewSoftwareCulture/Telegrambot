from bot_config import bot
from actions.get_weather import moskow
from actions.get_weather import spb
from actions.get_weather import istra
from actions.get_weather import tlt
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
        elif message.text.lower() == 'погода':
            bot.send_message(message.chat.id, 'Выбери город', reply_markup=keyboards.menu_weather)
        elif message.text == 'Москва 🌍':
            bot.send_message(message.chat.id, moskow())
        elif message.text == 'Истра 🌍':
            bot.send_message(message.chat.id, istra())
        elif message.text == 'Тольятти 🌍':
            bot.send_message(message.chat.id, tlt())
        elif message.text == 'Питер 🌍':
            bot.send_message(message.chat.id, spb())
        elif message.text.lower() == 'aliance':
            bot.send_message(message.chat.id, 'За Альянс!', reply_markup=keyboards.menu_Aliance)
        elif message.text.lower() == 'horge':
            bot.send_message(message.chat.id, "Lok'tar Ogar", reply_markup=keyboards.menu_Horge)