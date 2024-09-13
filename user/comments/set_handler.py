from aiogram import types

from loader import dp
from services.services import getUser
from states import Comments
from asyncio import create_task
from aiogram.dispatcher import FSMContext
from utils import buttons, texts

async def comment_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    
    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    if user['lang'] == "uz":
        await message.answer(texts.COMMENT_BALL_UZ, reply_markup=buttons.COMMENT_STATUS_UZ)
    elif user['lang'] == "ru":
        await message.answer(texts.COMMENT_BALL_RU, reply_markup=buttons.COMMENT_STATUS_RU)
    else:
        await message.answer(texts.COMMENT_BALL_EN, reply_markup=buttons.COMMENT_STATUS_EN)

    await Comments.commen_ball.set()

@dp.message_handler(
    lambda message: message.text.startswith(buttons.MENU_FEEDBACK_UZ) or \
                    message.text.startswith(buttons.MENU_FEEDBACK_RU) or \
                    message.text.startswith(buttons.MENU_FEEDBACK_EN)
)
async def func(message: types.Message, state: FSMContext):
    await create_task(comment_handler(message, state))



