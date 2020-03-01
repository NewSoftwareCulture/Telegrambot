from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


from bot_config import tg_token
from bot_config import tg_api_url

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.messege.chat_id,
        text="Привет! Отправь мне что-нибудь",
    )

def do_echo(bot: Bot, update: Update):
    text=update.messege.text
    bot.send_message(
        chat_id=update.messege.chat_id,
        text=text,
    )

def main():
    bot = Bot (
        token = tg_token,
        base_url=tg_api_url,
    )
    updater = Updater (
        bot = bot,
    )

    start_hendler = CommandHandler("start", do_start)
    messege_hendler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_hendler)
    updater.dispatcher.add_handler(messege_hendler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()