from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from services.services import getCategorys, getFoods, getUser

from states import FoodOrder
from user.basket.user_basket import user_basket
from user.delivery.set_handler import deliver_food
from user.menu import MainMenu
from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    Tanlanga categoriyadagi maxsulotlar
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    category_name = message.text

    # categoryalarni olish
    foods = getFoods(category=category_name)

    # xato categorya yuborilsa uni o'chirib tashlash
    if not bool(foods):
        # await message.delete()
        if message.text.startswith((buttons.BASKET_UZ, buttons.BASKET_RU, buttons.BASKET_EN)):
            await user_basket(message, state)
        if message.text.startswith((buttons.DELIVER_UZ, buttons.DELIVER_RU, buttons.DELIVER_EN)):
            await deliver_food(message, state)

        return

    # categoryiga doir maxsulotlarni yuborish
    await message.answer(text=texts.FOODS[lang], reply_markup=buttons.FOODS_BUTTONS(foods, lang))

    print("foods State: ", await state.get_data())
    await state.update_data({
        'category': category_name
    })

    # stateni foodga o'tqazish
    await FoodOrder.food.set()
    print("foods State: ", await state.get_data())


@dp.message_handler(state=FoodOrder.category)
async def foods(message: types.Message, state: FSMContext):
    if message.text in (buttons.CATEGORY_BACK_UZ, buttons.CATEGORY_BACK_RU, buttons.CATEGORY_BACK_EN):
        await MainMenu(message, state)
    else:
        await create_task(_task(message, state))
