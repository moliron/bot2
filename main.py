from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('hi', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'отправить кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://gas-kvas.com/grafic/uploads/posts/2023-09/1695802650_gas-kvas-com-p-kartinki-kot-7.jpg', caption='cat')

@dp.message_handler(lambda message: message.text == 'перейти на след клав')
async def button_2_click(message: types.Message):
    await message.answer('тут можно отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text =='отправить собаку')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/i?id=791394c592073be28cc0740a790fdcda_l-5234597-images-thumbs&n=13', caption='dog')

@dp.message_handler(lambda message: message.text == 'перейти обратно')
async def button_2_click(message: types.Message):
    await message.answer('тут можно вернутся обратно', reply_markup= get_keyboard_1())

if __name__ != '__name__':
    executor.start_polling(dp, skip_updates=True)