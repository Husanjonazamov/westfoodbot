from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from services.services import clearBasketAndSetRating, getUser, getCategorys

from user.orderd.start_order import order
from utils import buttons, texts

from states import FoodOrder


async def _task(message: types.Message, state: FSMContext):
    """
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']


    print("Message received:", message.text)  # Debugging uchun
    print("Back button pressed:", message.text)  # Debugging uchun
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    category = getCategorys()
    state_data = await state.get_data()
    await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
    await FoodOrder.category.set()
    print("Other button pressed:", message.text)  # Debugging uchun

    # Har bir bosqichdan so'ng state holatini tekshiramiz
    current_state = await state.get_state()
    print("Current stsadsdsdsdsdate:", current_state)


@dp.message_handler(
    lambda message: any(message.text.startswith(prefix) for prefix in [
        buttons.BASKET_BACK_BUTTON_UZ,
        buttons.BASKET_BACK_BUTTON_RU,
        buttons.BASKET_BACK_BUTTON_EN,
    ]),
    content_types=['text'], state="*"
)
async def order(message: types.Message, state: FSMContext):
    await create_task(_task(message, state))
