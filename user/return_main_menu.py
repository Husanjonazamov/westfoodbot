
print("1. Init back...")

from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from states import Register
from services.services import getCategorys, getUser
from user.menu import MainMenu
from utils import buttons, texts

from states import FoodOrder

async def _task(message: types.Message, state: FSMContext):
    """
    """ 

    # user id
    user_id = message.from_user.id

    current_state = await state.get_state()
    print(current_state)
    print(type(current_state))
    
    await MainMenu(message, state)

@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.RETURN_MAIN_MENYU_UZ,   
            buttons.RETURN_MAIN_MENYU_RU,   
            buttons.RETURN_MAIN_MENYU_EN,
        )),
        state='*')
async def back(message: types.Message, state: FSMContext):
    create_task(_task(message, state))



@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.RETURN_MAIN_MENYU_TXT_UZ,
                buttons.RETURN_MAIN_MENYU_TXT_RU,
                buttons.RETURN_MAIN_MENYU_TXT_EN,
                )), state="*", content_types=['text'])
async def deliver_food(message: types.Message, state: FSMContext):
    print("🎳 ~ set_attribution.py:13 -> state: ",  state)
    user_id = message.from_user.id

    user = getUser(user_id)
    lang = user['lang']
    
    category = getCategorys()
            # categoryani yuborish
    await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
    await FoodOrder.category.set()

