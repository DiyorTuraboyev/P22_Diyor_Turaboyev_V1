from aiogram.filters import CommandStart
import asyncio
import logging
import sys
from aiogram.types import Message
from const import dp, bot
from database.db_functions import set_users_to_redis, get_user_date
from utils.bot_commands import get_bot_commands
from admin.handlers import state_router, send_router
from keyboards.reply import menu_kbs


@dp.message(CommandStart())
async def start(message: Message):
    menu_kb = menu_kbs(message)
    commands = get_bot_commands(message)
    await bot.set_my_commands(commands)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\nxush kelibsiz", reply_markup=menu_kb)
    user_data = get_user_date(str(message.from_user.id))
    if not user_data:
        set_users_to_redis(user_id=str(message.from_user.id), name=str(message.from_user.full_name))


async def main():
    dp.include_routers(state_router, send_router)
    await dp.start_polling(bot, polling_timeout=2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
