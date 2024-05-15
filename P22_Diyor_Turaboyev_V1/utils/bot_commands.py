from aiogram.types import BotCommand, Message
from const import admin_list


def get_bot_commands(message: Message):
    bot_command = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
    ]
    if str(message.from_user.id) in admin_list:
        send_command = [BotCommand(command='/send', description="Sends message to user"),
                        BotCommand(command='/stat', description="Shows user data")]
        bot_command.extend(send_command)
        print(bot_command)
        return bot_command
    return bot_command

