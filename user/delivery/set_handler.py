from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from asyncio import create_task
from aiogram.types import CallbackQuery

from states import Delivery
from services.services import getBasketList, getUser
from utils import texts, buttons


async def delivery_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']

    basket = getBasketList(user_id)

    if not basket:
        await message.answer(text=texts.EMPTY_BASKET[lang])
        return

    await message.answer(texts.DELEVERY_COMMENT_TEXT[lang], reply_markup=buttons.DELIVERY_SET_BUTTON[lang])

    await state.set_state(Delivery.addComment)

@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.DELIVER_UZ,
                buttons.DELIVER_RU,
                buttons.DELIVER_EN,
                )), state="*", content_types=['text'])
async def deliver_food(message: Message, state: FSMContext):
    create_task(delivery_task(message, state))