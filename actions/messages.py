from bot_config import bot

def functions():
    @bot.message_handler(
        content_types=['text'],
    )
    def func(message):
        print(message.text.lower().find('id'))
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + ", я тут местный бот")
        if message.text.lower().find('id') > -1:
            bot.send_message(message.chat.id, "Твой ID: " + str(message.from_user.id))