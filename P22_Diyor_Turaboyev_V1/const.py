from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import redis

load_dotenv()
TOKEN = getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


r = redis.Redis(host='localhost', port=6379, db=0) # you need to connect with your redis database


admin_list = ['1670352901'] # you can add admins to here
