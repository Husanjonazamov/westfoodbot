from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from asyncio import create_task
from aiogram.types import CallbackQuery

from states import Delivery, FoodOrder
from services.services import getBasketList, getUser, getCategorys
from utils import texts, buttons




async def add_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    phone = user['phone']

    lang = user['lang']
    data = await state.get_data()
    add_note = data.get('add_note')
    location_name = data.get('location_name')
    basket = getBasketList(user_id)
    add_note=message.text


    await state.update_data({
        'add_note': add_note,
    })

    print(
        await state.get_data()
    )

    basket = getBasketList(user_id)

    if not basket:
        await message.answer(text=texts.EMPTY_BASKET[lang])
        return

    await message.answer(texts.PAYMENT[lang], reply_markup=buttons.PAYMENT_BUTTONS[lang])


    await state.set_state(Delivery.payment)




@dp.message_handler(state=Delivery.addComment, content_types=['text'])
async def addcommit_delivery(message: Message, state: FSMContext):
        print("Message received:", message.text)  # Debugging uchun
        if message.text in [buttons.DELIVERY_MENU_UZ, buttons.DELIVERY_MENU_RU, buttons.DELIVERY_MENU_EN]:
            print("Back button pressed:", message.text)  # Debugging uchun
            user_id = message.from_user.id
            user = getUser(user_id)
            lang = user['lang']
            state_data = await state.get_data()
            category = getCategorys()
            # categoryani yuborish
            await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
            await FoodOrder.category.set()
        elif message.text in [buttons.DELIVERY_COMMENT_BACK_UZ, buttons.DELIVERY_COMMENT_BACK_RU, buttons.DELIVERY_COMMENT_BACK_EN]:
            print("Back button pressed:", message.text)  # Debugging uchun
            user_id = message.from_user.id
            user = getUser(user_id)
            lang = user['lang']
            state_data = await state.get_data()
            category = getCategorys()
            # categoryani yuborish
            await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
            await FoodOrder.category.set()
        else:
            print("Other button pressed:", message.text)  # Debugging uchun
            await create_task(add_task(message, state))

        # Har bir bosqichdan so'ng state holatini tekshiramiz
        current_state = await state.get_state()
        print("Current state set_add:", current_state)
