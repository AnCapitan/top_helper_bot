import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TOKEN_TELEGRAM = os.environ.get('TOKEN_TELEGRAM')
GROUPADMIN = os.environ.get('GROUPADMIN')
GROUPDIRECTOR = os.environ.get('GROUPDIRECTOR')
GROUP_EDUCATIONAL = os.environ.get('GROUP_EDUCATIONAL')
bot = TeleBot(TOKEN_TELEGRAM, threaded=False)

