from bot_config import bot
from actions.get_gismeteo import weather

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