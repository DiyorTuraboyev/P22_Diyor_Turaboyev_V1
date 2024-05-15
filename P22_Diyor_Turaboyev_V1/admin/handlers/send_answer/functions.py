from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.reply import show_user_ids_kb, menu_kbs
from const import admin_list
from .states import Send


async def send_answer(message: Message, state: FSMContext):
    menu_kb = menu_kbs(message)
    if not str(message.from_user.id) in admin_list:
        await message.answer("You need to be admin to use this command", reply_markup=menu_kb)
        await state.clear()
        return
    else:
        user_ids_kb = show_user_ids_kb()
        await state.set_state(Send.send_answer)
        await message.answer("To send message to user\nYou need to click one of user's Id from below",
                             reply_markup=user_ids_kb)


async def get_message(message: Message, state: FSMContext):
    await state.update_data(get_user_id=str(message.text))
    await state.set_state(Send.send_message)
    await message.answer("Now, enter your message that\n"
                         "You wanted to send to user 📩")


async def send_message(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    menu_kb = menu_kbs(message)
    user_id = data['get_user_id']
    try:
        await bot.send_message(chat_id=str(user_id), text=str(message.text))
        await message.answer("Your message was sent to user ✅\nThanks", reply_markup=menu_kb)
        await state.clear()
    except Exception as e:
        await message.answer("You entered incorrect user ID", reply_markup=menu_kb)
        print(e)

