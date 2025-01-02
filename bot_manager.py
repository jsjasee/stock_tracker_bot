from telebot import TeleBot
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

class BotManager:
    def __init__(self):
        self.bot = TeleBot(token=TOKEN)

    def send_message(self, message):
        self.bot.send_message(chat_id=CHAT_ID, text=message)
