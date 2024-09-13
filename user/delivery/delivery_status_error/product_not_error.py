from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from services.services import getUser, getBasketList, clearBasketAndSetRating


from utils.functions import calculate_distance, create_google_maps_link
from states import Delivery
from utils.constantas import KITCHEN_LAN, KITCHEN_LON

from utils import texts, buttons



def format_price(price):
    return f"{price:,}".replace(',', ' ')


async def handle_take_succes_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    user_id = data_split[1].replace("user_id:", "")
    old_message_text = call.message.text
    message_id = call.message.message_id

    user = getUser(user_id)
    lang = user['lang']

    
    fullname = user['fullname']
    phone = user['phone']
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



    await bot.send_message(
        chat_id=user_id,
        text=texts.NEW_DELIVER_ERROR_EMPTY_FOOD[lang]
    )

    await call.message.edit_text(
        text=texts.NEW_DELIVERY(
            basket=formatted_basket, fullname=fullname, phone=phone, add_note=add_note, payment_type=payment_type, location_name=location_name,
            ),
        # reply_markup=buttons.REMOVE_TAKE(message_id, user_id)
    )
    clearBasketAndSetRating(user_id)


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("not_product:"), state="*")
async def handle_take_succes(callbask_query: CallbackQuery, state: FSMContext):
    create_task(handle_take_succes_task(callbask_query, state))
