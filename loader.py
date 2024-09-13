import os
import dotenv
import logging
from aiogram import Bot, Dispatcher
import django
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django .setup()

storage = MemoryStorage()

# API_TOKEN = os.getenv('API_TOKEN')
API_TOKEN = '6054331702:AAFAVTyWtSQHHYqrRnctBE5_Tf9X87do8-w'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)