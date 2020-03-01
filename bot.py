from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from config import tg_token

def main():
    bot = Bot (
        token = tg_token,
    )
