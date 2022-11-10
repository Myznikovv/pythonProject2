import logging
import openpyxl
import config as cfg
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello, "+ str(message.from_user.first_name)+ "! This your bot" )


@dp.message_handler()
async def mess(message: types.Message):
    if message.text == "id":
        await bot.send_message(message.from_user.id, message.from_user.id)
        await bot.send_message(message.from_user.id, message.from_user.username)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
