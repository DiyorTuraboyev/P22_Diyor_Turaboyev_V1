from aiogram import Router
from aiogram.filters import Command
from .states import State
from .functions import state_command_answer, show_user_data

state_router = Router()


state_router.message.register(state_command_answer, Command('stat'))
state_router.message.register(show_user_data, State.show_user_registered_date_and_time)
