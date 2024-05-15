from aiogram import Router
from aiogram.filters import Command
from .states import Send
from .functions import send_answer, get_message, send_message

send_router = Router()


send_router.message.register(send_answer, Command('send'))
send_router.message.register(get_message, Send.send_answer)
send_router.message.register(send_message, Send.send_message)
