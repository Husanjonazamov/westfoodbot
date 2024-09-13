from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from services.services import addBasket, getUser, getCategorys, getFoods

from states import FoodOrder
from utils import buttons
from utils import texts

async def _task(message: types.Message, state: FSMContext):
    """
    Bitta maxsulotni ko'rish
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    # xato raqam yuborilsa uni o'chirib tashlash
    count = message.text

    if not count.isdigit():
        await message.delete()

    state_data = await state.get_data()
    food_name = state_data['food_name']
    # basketga qo'shish

    # basketga qo'shish
    addBasket(user_id, food_name, count)

    await state.set_state(FoodOrder.category)

    category = getCategorys()

    # categoryani yuborish
    await message.answer(text=texts.ORDER_RESET[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
    await state.set_state(FoodOrder.category)

    print("food quanty State: ", await state.get_data())


@dp.message_handler(state=FoodOrder.count)
async def food_quantity(message: types.Message, state: FSMContext):
    if message.text in (buttons.FOOD_BACK_UZ, buttons.FOOD_BACK_RU, buttons.FOOD_BACK_EN):
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']
        state_data = await state.get_data()
        category = state_data.get('category')
        foods = getFoods(category=category)
        await message.answer(texts.FOODS[lang], reply_markup=buttons.FOODS_BUTTONS(foods, lang))
        await FoodOrder.food.set()

    else:
        create_task(_task(message, state))
