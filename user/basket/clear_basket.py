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
    User basketdan ovqatni o'chirish
    """
    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']
    category = getCategorys()
    clearBasketAndSetRating(user_id)

    await message.answer(texts.CLEAR_BASKET[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
    await state.set_state(FoodOrder.category)
    print(f"State set to: {await state.get_state()}")  # Debugging uchun

@dp.message_handler(
    lambda message: any(message.text.startswith(prefix) for prefix in [
        buttons.CLEAR_BASKET_UZ,
        buttons.CLEAR_BASKET_RU,
        buttons.CLEAR_BASKET_EN,
        '🆑 Savatni tozalash'
    ]),
    state='*'
)
async def clear_basket(message: types.Message, state: FSMContext):
    print("Clear basket button pressed...")  # Debugging uchun
    await create_task(_task(message, state))
    print(f"Current state after clearing basket: {await state.get_state()}")  # Debugging uchun
