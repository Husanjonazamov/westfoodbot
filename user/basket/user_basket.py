print("1. user_basket...")

from aiogram import types
from aiogram.dispatcher import FSMContext
from asyncio import create_task
from loader import dp
from services.services import getBasketList, getUser, getCategorys
from utils import buttons, texts
from states import FoodOrder, Basket

def format_price(price):
    return f"{price:,}".replace(',', ' ')

async def _task(message: types.Message, state: FSMContext):
    """
    User basketdan ovqatni o'chirish
    """
    print("Starting _task...")  # Debugging uchun
    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']
    user_basket = getBasketList(user_id)
    category = getCategorys()

    if not user_basket:
        await message.answer(text=texts.EMPTY_BASKET[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
        await state.set_state(FoodOrder.category)
        print(f"State set to: {await state.get_state()}")  # Debugging uchun
        return

    if lang == 'uz':
        await message.answer(texts.USER_BASKET_TZ[lang])
        answer_text = "📥 Savat:\n"
        total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi

        for i in user_basket:
            item_name = i['food']['name_uz']
            item_count = i['count']
            item_price = i['food']['price']
            item_total = item_count * item_price

            formatted_item_price = format_price(item_price)
            formatted_item_total = format_price(item_total)

            answer_text += f"\n{item_name}\n"
            answer_text += f"{item_count} X {formatted_item_price} so'm = {formatted_item_total} so'm\n"

            total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

        formatted_total_price = format_price(total_price)
        # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
        answer_text += f"\nUmumiy narx: {formatted_total_price} so'm\n"

    elif lang == 'ru':
        await message.answer(texts.USER_BASKET_TZ[lang])

        answer_text = "📥 Корзина:\n"
        total_price = 0
        for i in user_basket:
            item_name = i['food']['name_uz']
            item_count = i['count']
            item_price = i['food']['price']
            item_total = item_count * item_price

            formatted_item_price = format_price(item_price)
            formatted_item_total = format_price(item_total)

            answer_text += f"\n{item_name}\n"
            answer_text += f"{item_count} X {formatted_item_price} Cym = {formatted_item_total} Cym\n"

            total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

        formatted_total_price = format_price(total_price)
        # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
        answer_text += f"\nОбщая стоимость: {formatted_total_price} Cym\n"

    elif lang == 'en':
        await message.answer(texts.USER_BASKET_TZ[lang])

        answer_text = "📥 Basket:\n"
        total_price = 0
        for i in user_basket:
            item_name = i['food']['name_uz']
            item_count = i['count']
            item_price = i['food']['price']
            item_total = item_count * item_price

            formatted_item_price = format_price(item_price)
            formatted_item_total = format_price(item_total)

            answer_text += f"\n{item_name}\n"
            answer_text += f"{item_count} X {formatted_item_price} Soum = {formatted_item_total} Soum\n"

            total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

        formatted_total_price = format_price(total_price)
        # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
        answer_text += f"\nTotal price: {formatted_total_price} Soum\n"

    await message.answer(text=answer_text, reply_markup=buttons.USER_BASKET(user_basket, lang))
    print("Finishing task...")  # Debugging uchun
    await state.set_state(Basket.clear)  # Yangi holatga o'tish
    print(f"State set to: {await state.get_state()}")  # Debugging uchun



@dp.message_handler(
    lambda message: any(message.text.startswith(prefix) for prefix in [
        buttons.BASKET_UZ,
        buttons.BASKET_RU,
        buttons.BASKET_EN,
        '🛒 Корзина'
    ]),
    state="*"
)
async def user_basket(message: types.Message, state: FSMContext):
    print("Basket button pressed...")  # Debugging uchun
    await create_task(_task(message, state))
    current_state = await state.get_state()
    print("Current state after setting new state:", current_state)  # Debugging uchun
