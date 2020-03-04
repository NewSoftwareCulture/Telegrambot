from bot_config import bot
from actions.get_weather import weather
from keyboards import menu_Aliance
from keyboards import menu_Horge

def functions():
    @bot.message_handler(
        content_types=['text'],
    )
    def func(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, "Привет, @" + message.from_user.username + ", я тут местный бот")
        if message.text.lower().find('id') > -1:
            bot.send_message(message.chat.id, "Твой ID: " + str(message.from_user.id))
        if message.text.lower() == 'погода':
            bot.send_message(message.chat.id, weather())
        if message.text.lower() == 'aliance':
            bot.send_message(message.chat.id, 'За Альянс!', reply_markup=menu_Aliance)
        if message.text.lower() == 'horge':
            bot.send_message(message.chat.id, "Rok'Tar Ogar!", reply_markup=menu_Horge)