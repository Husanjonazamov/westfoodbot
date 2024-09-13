from aiogram.dispatcher.storage import FSMContext
from loader import dp
from asyncio import create_task
from aiogram.types import CallbackQuery
from pyclick import PyClick
from states import Delivery
from services.services import getBasketList, getUser
from utils import texts, buttons


async def process_payment_task(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = getUser(user_id)
    basket = getBasketList(user_id)
    total_price = sum(item['food']['price'] * item['count'] for item in basket)

    # Click to'lov tizimi uchun URL ni yaratamiz
    return_url = 'http://127.0.0.1:8000/'  # To'lovdan keyingi qaytish URL manzili
    order_id = 1  # Bu yerda sizning order ID bo'lishi kerak
    url = PyClick.generate_url(order_id=order_id, amount=str(total_price), return_url=return_url)

    await call.message.answer(f"To'lov uchun quyidagi havolaga o'ting: {url}")

    # Callback queryni javobini tozalaymiz
    await call.answer()



@dp.callback_query_handler(lambda call: call.data == 'make_payment')
async def process_payment(call: CallbackQuery, state: FSMContext):
  create_task(process_payment_task(call, state))