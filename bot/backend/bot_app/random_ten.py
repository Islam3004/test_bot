from aiogram import types
from . bot import dp
from . keyboards import inline_kb

@dp.message_handler(commands="train_ten")
async def train_ten(message: types.Message):
    await GameStates.random_ten.set()
    # res = await get_random()
    await message.reply('train_ten', reply_markup=inline_kb)
