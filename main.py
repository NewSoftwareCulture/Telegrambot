import requests
from bot_config import bot
from bot_config import channel_name
import actions

def main():
    while True:
        try:
            actions.commands()
            actions.messages()
            
            bot.infinity_polling(True) 

        except Exception as e:
            error_code = "C3PO_bot! \n\nError: \n" + str(e)
            print(error_code)  # или просто print(e) если у вас логгера нет,
            bot.send_message(channel_name, error_code) 

if __name__ == '__main__':
    main()