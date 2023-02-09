import time
import logging

from random import randint
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5624470339:AAGIXfmDQ_U5rXOm5ax9-JCzGH9AsPOJBBc'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def start_handler(message: types.Message, usr=None):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name}', time.asctime())

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
@dp.message_handler(commands = 'start')

async def send_welcome(message: types.Message):
    urlkb = InlineKeyboardMarkup(row_width=2)
    urlButton = InlineKeyboardButton(text='$',  callback_data="dollar")
    urlButton2 = InlineKeyboardButton(text='€',  callback_data="euro")
    urlButton3 = InlineKeyboardButton(text='¥',  callback_data="yen")
    urlkb.add(urlButton,urlButton2,urlButton3)
    await bot.send_message(message.from_user.id, 'Привет!\nКурс какой валюты ты хочешь узнать?', reply_markup=urlkb)

@dp.callback_query_handler()
async def euro(call: types.CallbackQuery) :
    a = randint(0, 100)
    await bot.send_message(call.from_user.id,  a)

@dp.callback_query_handler()
async def euro(call: types.CallbackQuery) :
    a = randint(0, 100)
    await bot.send_message(call.from_user.id,  a)

@dp.callback_query_handler()
async def euro(call: types.CallbackQuery) :
    a = randint(0, 100)
    await bot.send_message(call.from_user.id,  a)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)