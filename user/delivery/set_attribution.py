from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from loader import dp, bot
from asyncio import create_task
from payments.views import OrderCheckAndPayment
from services.services import getBasketList, getUser, getUserPhone
from user.basket.user_basket import user_basket
from utils.functions import calculate_distance, create_google_maps_link
from states import Delivery
from utils.constantas import ORDER_SEND_CHAT, ORDER_DELIVERY_MESSAGE_THREAD_ID, KITCHEN_LAN, KITCHEN_LON
from utils import texts, buttons
from pyclick import PyClick
from aiogram.types import ReplyKeyboardRemove
from asgiref.sync import sync_to_async



def format_price(price):
    return f"{price:,}".replace(',', ' ')




async def delivery_att_task(message: Message, state: FSMContext):
    print("🎳 ~ set_attribution.py:13 -> state: ",  state)
    user_id = message.from_user.id

    user = getUser(user_id)
    lang = user['lang']
    fullname = user['fullname']
    phone = user['phone']
    data = await state.get_data()
    basket = getBasketList(user_id)

    total_price = 0
    for i in basket:
        total_price += i['food']['price'] * i['count']

    return_url = 'https://t.me/west_uzbot'  # To'lovdan keyingi qaytish URL manzili
    url = PyClick.generate_url(order_id=user_id, amount=str(total_price), return_url=return_url)

    add_note = data.get('add_note')
    payment_type = data.get('payment_type')
    location = data.get('location')
    location_name = data.get('location_name')

    isClick = '💳 Click' in payment_type
    isPayme = '💳 Payme' in payment_type
    print(isPayme)
    print(isClick)

    print("🛡️ ~ set_attribution.py:24 -> location: ",  location)

    user_latitude = location['latitude']
    user_longitude = location['longitude']
    zoom_level = 16

    distance = calculate_distance(
        user_latitude,
        user_longitude,
        KITCHEN_LAN,
        KITCHEN_LON,
    )

    maps_link = create_google_maps_link(user_latitude, user_longitude, zoom_level)

    formatted_basket = [
        {
            'food': i['food'],
            'count': i['count'],
            'formatted_price': format_price(i['food']['price']),
            'formatted_total': format_price(i['count'] * i['food']['price'])
        }
        for i in basket
    ]



    if isClick:
        await bot.send_message(
            chat_id=user_id,
            text=texts.SUCCES_PAYMENT[lang],
            reply_markup=buttons.get_payment_button(lang, url)
        )
        
        await message.answer(
            text=texts.REMOVE_BUTTON[lang],
            reply_markup=ReplyKeyboardRemove()
        )
        await Delivery.click.set()
            
    else:
        await bot.send_message(
            chat_id=user_id,
            text=texts.ORDER_SUCCES_SEND_ADMIN[lang],
            reply_markup=buttons.RETURN_MAIN_BUTTON_MENU[lang]
        )
        await bot.send_message(
            chat_id=ORDER_SEND_CHAT,
            text=texts.NEW_DELIVERY(
                distance=distance,
                basket=formatted_basket, fullname=fullname, phone=phone, add_note=add_note, payment_type=payment_type, location_name=location_name,
                maps_link=maps_link),
            reply_to_message_id=ORDER_DELIVERY_MESSAGE_THREAD_ID,
            reply_markup=buttons.NEW_DELIVERY(user_id, distance, maps_link)
        )

        # await state.update_data(order_sent=True)  # Buyurtma yuborilganini belgilash
        await state.finish()

@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.ORDER_CHECK_UZ,
                buttons.ORDER_CHECK_RU,
                buttons.ORDER_CHECK_EN,
                )), state=Delivery.attribution_send, content_types=['text'])
async def deliver_food(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get('order_sent'):
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']
        await message.answer(texts.ORDER_ALREADY_SENT[lang])
    else:
        await state.update_data(order_sent=True)
        await create_task(delivery_att_task(message, state))

@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.ORDER_ОТМЕНА_UZ,
                buttons.ORDER_ОТМЕНА_RU,
                buttons.ORDER_ОТМЕНА_EN,
                )), state=Delivery.attribution_send, content_types=['text'])
async def cancel_delivery(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']
    
    await message.answer(texts.PAYMENT[lang], reply_markup=buttons.PAYMENT_BUTTONS[lang])
    await state.set_state(Delivery.payment)
