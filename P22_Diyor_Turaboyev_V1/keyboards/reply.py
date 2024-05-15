from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database.db_functions import get_all_user_ids
from const import admin_list


def show_user_ids_kb():
    user_ids = get_all_user_ids()
    users_kb = ReplyKeyboardBuilder()
    for user_id in user_ids:
        users_kb.button(text=user_id)
    users_kb.adjust(2, repeat=True)
    users_kb = users_kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    return users_kb


def menu_kbs(message: Message):
    user_id = str(message.from_user.id)
    menu_kb = ReplyKeyboardBuilder()
    menu_kb.button(text='/start')
    if user_id in admin_list:
        menu_kb.button(text='/send')
        menu_kb.button(text='/stat')
    menu_kb.adjust(1, repeat=True)
    menu_kb = menu_kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    return menu_kb


