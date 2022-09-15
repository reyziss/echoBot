"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5406714370:AAE-GOxutqGkHE6xxDD3n2KieQimIkdi2P4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("wassup!\nI'm komar!\npowered by krasyuk.")

@dp.message_handler(commands=['help'])
async def support(message: types.Message):
    await message.answer("wassup!\nI'm komar!\npowered by krasyuk.")

@dp.message_handler(commands=['photo'])
async def send_welcome(message: types.Message):
    await message.answer_photo('https://files.realpython.com/media/flow-new.0a9432c705ad.png')

@dp.message_handler(commands=['dice'])
async def send_welcome(message: types.Message):
     await message.answer_dice()

@dp.message_handler(commands=['location'])
async def send_welcome(message: types.Message):
         await message.answer_location('latitude', 'longitude')

@dp.message_handler()
async def welcome(message: types.Message):
    print()
    await message.answer(message.text + "\n😂 " + message.from_user.first_name)


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)