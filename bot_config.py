import telebot

token = '1004271213:AAGOzwDODpXHyF-bkf7wwFKyUoWwdkRdcgk'
channel = 'for_test_bots'
chat = 'test_for_bots_chat'

channel_name = '@' + channel
channel_id = 'https://t.me/' + channel

chat_name = '@' + chat
chat_id = 'https://t.me/' + chat


bot = telebot.TeleBot(token, threaded=False)