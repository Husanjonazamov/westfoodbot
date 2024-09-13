from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from asyncio import create_task
from aiogram.types import CallbackQuery

from states import Delivery, FoodOrder
from services.services import getBasketList, getUser, getCategorys
from utils import texts, buttons

payment_type = None

def format_price(price):
    return f"{price:,}".replace(',', ' ')

async def add_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    phone = user['phone']
    fullname = user['fullname']
    lang = user['lang']
    data = await state.get_data()
    add_note = data.get('add_note')
    location_name = data.get('location_name')
    basket = getBasketList(user_id)

    payment_type = message.text  # payment_type ni foydalanuvchidan olamiz va global o'zgaruvchiga saqlaymiz

    await state.update_data({'payment_type': payment_type})

    basket = getBasketList(user_id)

    if not basket:
        await message.answer(text=texts.EMPTY_BASKET[lang])
        return

    formatted_basket = [
        {
            'food': i['food'],
            'count': i['count'],
            'formatted_price': format_price(i['food']['price']),
            'formatted_total': format_price(i['count'] * i['food']['price'])
        }
        for i in basket
    ]

    if lang == "uz":
        await state.set_state(Delivery.attribution_send)
        await message.answer(
            text=texts.USER_DELIVERY_ATTRIBUTION_UZ(
                basket=formatted_basket,
                phone=phone,
                fullname=fullname,
                add_note=add_note,
                payment_type=payment_type,
                location_name=location_name
            ),
            reply_markup=buttons.ORDER_ATTRIBUTION[lang]
        )
    elif lang == "en":
        await state.set_state(Delivery.attribution_send)
        await message.answer(
            text=texts.USER_DELIVERY_ATTRIBUTION_EN(
                basket=formatted_basket,
                phone=phone,
                fullname=fullname,
                add_note=add_note,
                payment_type=payment_type,
                location_name=location_name
            ),
            reply_markup=buttons.ORDER_ATTRIBUTION[lang]
        )
    else:
        await state.set_state(Delivery.attribution_send)
        await message.answer(
            text=texts.USER_DELIVERY_ATTRIBUTION_RU(
                basket=formatted_basket,
                phone=phone,
                fullname=fullname,
                add_note=add_note,
                payment_type=payment_type,
                location_name=location_name
            ),
            reply_markup=buttons.ORDER_ATTRIBUTION[lang]
        )

    await state.set_state(Delivery.attribution_send)


@dp.message_handler(state=Delivery.payment, content_types=['text'])
async def addcommit_delivery(message: Message, state: FSMContext):
    print("Message received:", message.text)  # Debugging uchun
    if message.text in [buttons.PAYMENT_MENU_UZ, buttons.PAYMENT_MENU_RU, buttons.PAYMENT_MENU_EN]:
        print("Back button pressed:", message.text)  # Debugging uchun
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']
        state_data = await state.get_data()
        category = getCategorys()
        # categoryani yuborish
        await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
        await FoodOrder.category.set()
    elif message.text in [buttons.PAYMENT_BACK_UZ, buttons.PAYMENT_BACK_RU, buttons.PAYMENT_BACK_EN]:
        print("Back button pressed:", message.text)  # Debugging uchun
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']
        state_data = await state.get_data()
        await message.answer(texts.DELEVERY_COMMENT_TEXT[lang], reply_markup=buttons.DELIVERY_SET_BUTTON[lang])
        await state.set_state(Delivery.addComment)
    else:
        print("Other button pressed:", message.text)  # Debugging uchun
        await create_task(add_task(message, state))

    # Har bir bosqichdan so'ng state holatini tekshiramiz
    current_state = await state.get_state()
    print("Current state set_pay:", current_state)
