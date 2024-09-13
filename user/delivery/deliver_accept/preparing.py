from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from services.services import getUser, getBasketList
from utils import texts, buttons
from utils.price_format import format_price




async def y_new_d_task(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    basket = getBasketList(user_id)

    data_spelit = call.data.split('-')
    user_id = data_spelit[1].replace("user_id:", "")

    dis = float(data_spelit[2].replace("dis:", ""))
    maps_link = call.message.reply_markup.inline_keyboard[-1][0]['url']

    user = getUser(user_id)
    lang = user['lang']
    fullname = user['fullname']
    phone = user['phone']
    
    # Holatni yuklab olish
    data = await state.get_data()
    # if data is None:
    #     await call.message.answer("Holat ma'lumotlari mavjud emas.")
    #     return
    split_data = call.message.text.split('\n')
    add_note = split_data[3].split(': ')[1]
    payment_type = split_data[4].split(': ')[1]
    location_name = split_data[5].split(': ')[1]
    location = data.get('location')

    print(add_note)
    print(location_name)
    print(payment_type)
    


    print("🛡️ ~ set_attribution.py:24 -> location: ", location)

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
            basket=formatted_basket, 
            fullname=fullname,
            phone=phone,
            add_note=add_note,
            payment_type=payment_type,
            location_name=location_name),
        reply_markup=buttons.PREPARING(user_id, dis, maps_link)
    )
    await bot.send_message(
        chat_id=user_id,
        text=texts.SUCCES_ADD[lang],
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("y_new_d:"), state='*')
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    await create_task(y_new_d_task(callbask_query, state))

