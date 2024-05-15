from aiogram.fsm.state import StatesGroup, State


class Send(StatesGroup):
    send_answer = State()
    get_user_id = State()
    send_message = State()
