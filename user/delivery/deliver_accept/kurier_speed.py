from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from utils import texts, buttons
from services.services import getBasketList, getUser
from utils.functions import calculate_distance, create_google_maps_link

from utils.constantas import ORDER_SEND_CHAT, ORDER_DELIVERY_MESSAGE_THREAD_ID, KITCHEN_LAN, KITCHEN_LON
from utils.price_format import format_price


async def y_new_d_task(call: CallbackQuery, state: FSMContext):

    data_spelit = call.data.split('-')
    user_id = data_spelit[1].replace("user_id:", "")
    phone_line = call.message.text.split('\n')[-1]

    user = getUser(user_id)
    lang = user['lang']

    dis = float(data_spelit[2].replace("dis:", ""))
    maps_link = call.message.reply_markup.inline_keyboard[-1][0]['url']
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
        text=texts.PREPARING_FOOD[lang],
    )

    await call.message.edit_text(
        text=texts.NEW_DELIVERY(
            basket=formatted_basket, fullname=fullname, phone=phone, add_note=add_note, payment_type=payment_type, location_name=location_name),
        reply_markup=buttons.DELIVER_SPEED(user_id, dis, maps_link)
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("preparing:"), state="*")
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
