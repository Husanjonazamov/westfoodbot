from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery

from asyncio import create_task

from loader import dp, bot
from services.services import getBasketList, getUser

from utils import texts, buttons
from utils.price_format import format_price




async def y_new_d_task(call: CallbackQuery, state: FSMContext):
    # send_deliver:-user_id:{}-delivered_time
    data_split = call.data.split('-')

    user_id = data_split[1].replace("user_id:", "")
    delivered_time = data_split[2].replace("del_time:", "")
    maps_link = call.message.reply_markup.inline_keyboard[-1][0]['url']
    phone_line = call.message.text.split('\n')[-1]

    user = getUser(user_id)
    lang = user['lang']

    fullname = user['fullname']
    phone = user['phone']
    data = await state.get_data()

    split_data = call.message.text.split('\n')

    add_note = split_data[3].split(': ')[1]
    payment_type = split_data[4].split(': ')[1]
    location_name = split_data[5].split(': ')[1]

    # getBasketList funksiyasidan qaytgan qiymatni tekshirish
    basket = getBasketList(user_id)
    print(basket)
    




    formatted_basket = [
        {
            'food': i['food'],
            'count': i['count'],
            'formatted_price': format_price(i['food']['price']),
            'formatted_total': format_price(i['count'] * i['food']['price'])
        }
        for i in basket
    ]



    # Increment rating

    await bot.send_message(
        chat_id=user_id,
        text=texts.EIGHT_ACCEPT_DELIVERY[lang].format(delivered_time, phone_line),
    )

    await call.message.edit_text(
        text=texts.NEW_DELIVERY(
            basket=formatted_basket, fullname=fullname, phone=phone, add_note=add_note, payment_type=payment_type, location_name=location_name,
            ),
        reply_markup=buttons.DELIVER_ERROR_BUTTONS(maps_link, user_id)
    )


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("eight_deliver:"), state="*")
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
