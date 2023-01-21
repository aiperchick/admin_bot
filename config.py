from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv('MY_TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)
