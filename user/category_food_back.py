from services.services import getUser, getCategorys
from user.orderd.start_order import order

print("1. Init back...")

from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from states import Register, FoodOrder

from user.menu import MainMenu
from utils import buttons, texts


async def _task(message: types.Message, state: FSMContext):
    """
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']

    current_state = await state.get_state()
    print(current_state)
    print(type(current_state))
    await order(message, state)
@dp.message_handler(
    lambda message: message.text.startswith((
            buttons.FOOD_BACK_UZ,
            buttons.FOOD_BACK_RU,
            buttons.FOOD_BACK_EN,
    )),
    state='*')
async def back(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
