from aiogram.types import Message
from asyncio import create_task
from aiogram.dispatcher import FSMContext

from loader import dp
from services.services import getUser
from utils import buttons, texts



async def contact(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)

    # menu yuborish
    await message.answer(texts.CONTACT[lang], reply_markup=buttons.INSTAGRAM)



@dp.message_handler(state='*', commands=['contact'])
async def func(message: Message, state: FSMContext):
    await create_task(contact(message, state))