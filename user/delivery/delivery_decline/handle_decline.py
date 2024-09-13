# aiogram import
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# kode import
from loader import dp
from services.services import getUser, getBasketList
from utils import texts, buttons
from utils.price_format import format_price

# add import
from asyncio import create_task




async def delivery_decline_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    user_id = data_split[1].replace("user_id:", "")

    try:
        # user malumotlarini bazadan olish
        user = getUser(user_id)
        lang = user['lang']
        fullname = user['fullname']
        phone = user['phone']
    
    except:
        raise Exception("User topilmadi")

    
    
    data = await state.get_data()
    split_data = call.message.text.split('\n')
    add_note = split_data[3].split(': ')[1]
    payment_type = split_data[4].split(': ')[1]
    location_name = split_data[5].split(': ')[1]

    basket = getBasketList(user_id)
    
    formatted_basket = [
        {
            'food': i['food'],
            'count': i['count'],
            'formatted_price': format_price(i['food']['price']),
            'formatted_total': format_price(i['count'] * i['food']['price'])
        }
        for i in basket
    ]


    await call.message.edit_text(
        text=texts.NEW_DELIVERY(
            basket=formatted_basket, fullname=fullname, phone=phone, add_note=add_note, payment_type=payment_type, location_name=location_name),
        reply_markup=buttons.DECLINE_DELIVERY_STATUS(
            user_id=user_id,
            lang=lang
        )
    )


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("n_new_d:"), state="*")
async def deliver_decline(callbask_query: CallbackQuery, state: FSMContext):
    create_task(delivery_decline_task(callbask_query, state))
