from aiogram import types
from aiogram.dispatcher import FSMContext
from asyncio import create_task
from loader import dp
from services.services import deleteBasket, getCategorys, getUser, getBasketList
from user.basket.user_basket import user_basket
from states import FoodOrder
from utils import buttons, texts


async def _task(message: types.Message, state: FSMContext):
    """
    User basketdan ovqatni o'chirish
    """
    # user id
    user_id = message.from_user.id

    # food name
    food_name = message.text.replace("❌", "").strip()
    user = getUser(user_id)
    lang = user['lang']
    category = getCategorys()
    print(f"Deleting basket item: {food_name} for user_id: {user_id}")

    deleteBasket(food_name=food_name, user_id=user_id)

    user_basket_items = getBasketList(user_id)

    if not user_basket_items:
        await message.answer(texts.CLEAR_BASKET[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
        await state.set_state(FoodOrder.category)
    else:
        await user_basket(message, state)


@dp.message_handler(lambda message: any(message.text.startswith(prefix) for prefix in ["❌"]), state="*")
async def user_basket_delete(message: types.Message, state: FSMContext):
    print(f"Message received: {message.text}")
    await create_task(_task(message, state))
