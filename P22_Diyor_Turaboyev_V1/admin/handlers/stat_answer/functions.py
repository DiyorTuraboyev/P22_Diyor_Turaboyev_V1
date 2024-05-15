from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from .states import State
from database.db_functions import get_user_date
from const import admin_list
from keyboards.reply import show_user_ids_kb, menu_kbs


async def state_command_answer(message: Message, state: FSMContext):
    if not str(message.from_user.id) in admin_list:
        menu_kb = menu_kbs(message)
        await message.answer("You need to be admin to use this command", reply_markup=menu_kb)
        await state.clear()
        return
    else:
        user_ids_kb = show_user_ids_kb()
        await message.answer("To see user's data you need to write or click one of user ID of users")
        await message.answer("Please click or write user ID", reply_markup=user_ids_kb)
        await state.set_state(State.show_user_registered_date_and_time)


async def show_user_data(message: Message, state: FSMContext):
    data = get_user_date(str(message.text))
    if data:
        menu_kb = menu_kbs(message)
        await message.answer(f"User registered date: {data['registered_date']}\n"
                         f"User registered time: {data['registered_time']}", reply_markup=menu_kb)
        await state.clear()
    else:
        menu_kb = menu_kbs(message)
        await message.answer("You entered wrong user ID or \n"
                             "Your entered user has not registered yet", reply_markup=menu_kb)

