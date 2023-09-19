import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = 'Your Bot Token'

bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm exo Bot")


@dp.message_handler()
async def exo(message: types.Message):
    await message.answer(message.text)
   



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
