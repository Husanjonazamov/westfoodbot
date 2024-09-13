print("2. start order...")
# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from services.services import getCategorys, getUser
from states import FoodOrder
from utils import buttons, texts
from utils.time_func import is_within_working_hours

# add import
from asyncio import create_task




async def _task(message: types.Message, state: FSMContext):
    """
    🛍 Buyurtma berish
    """

    # user id
    user_id = message.from_user.id
    

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    # categoryani yuborish
    await message.answer(text=texts.ORDER_LOCATION[lang], reply_markup=buttons.ORDER_LOCATION[lang])

    await FoodOrder.location.set()
    print("start order State: ", await state.get_data())

@dp.message_handler(
    lambda message: message.text.startswith((
                        buttons.MENU_ORDER_UZ,
                        buttons.MENU_ORDER_RU,
                        buttons.MENU_ORDER_EN,)
                        ),
    state='*')
async def order(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    if is_within_working_hours():
        create_task(_task(message, state))
    else:
        await message.answer(texts.COLOSE_RESTORAN[lang])

