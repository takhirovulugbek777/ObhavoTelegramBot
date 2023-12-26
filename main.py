from aiogram import types, Dispatcher, Bot, executor

token = "6654581861:AAGiVYTQJdKUZVXvrhisQgTJ7GI_Akb--XY"
from api import obhavo

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Assalomu alaykum! 🌞🌈 Bot sizga shahringizdagi ob-havo haqida yangi ma'lumotlar beradi! 🌍🔍 Siz bormoqchi bo'lgan shaharni ham. 🌤🌡\n"
                         "🔍 Shahar nomini yozing")



@dp.message_handler(content_types='text')
async def first_handler(message: types.Message):
    shahar = message.text
    data = obhavo(shahar)
    if data == 'Error':
        await message.answer("Malumot topilmadi!")
    else:
        await message.answer(data)


if __name__ == '__main__':
    executor.start_polling(dp)
