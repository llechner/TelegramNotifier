''' 
Some definitions.
Set up Telegram bot and ID according to
https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay

use https://api.telegram.org/bot<telegramBotToken>/getUpdates to get your telegramUserID

'''
import os
if os.environ['USER'] in ['llechner']:
    telegramBotToken = "975741952:AAE2M2IRHZkn850QikWdGejV9-GdbUctYmQ"
    telegramUserID = "198612695"
