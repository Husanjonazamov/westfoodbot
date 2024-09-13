
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from loader import dp, bot
from asyncio import create_task
from services.services import getBasketList, getUser
# from users.delivery.delivery_phone import phone_number
from utils.functions import calculate_distance, create_google_maps_link
from states import Delivery
from utils.constantas import ORDER_SEND_CHAT, ORDER_DELIVERY_MESSAGE_THREAD_ID, KITCHEN_LAN, KITCHEN_LON
from utils import texts, buttons


async def delivery_location_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    user = getUser(user_id)
    lang = user['lang']
    fullname = user['fullname']

    data = await state.get_data()
    phone = data.get('phone')
    basket = getBasketList(user_id)

    user_latitude = message.location.latitude
    user_longitude = message.location.longitude
    zoom_level = 16
    await state.update_data(location=message.location)

    distance = calculate_distance(
        user_latitude,
        user_longitude,
        KITCHEN_LAN,
        KITCHEN_LON,
    )

    maps_link = create_google_maps_link(user_latitude, user_longitude, zoom_level)

    # send message curier
    await bot.send_message(
        chat_id=ORDER_SEND_CHAT,
        text=texts.NEW_DELIVERY(
            distance=distance,
            basket=basket, phone=phone,
            maps_link=maps_link )+ f"\n👤 Mijozning ismi: {fullname}",
        reply_to_message_id=ORDER_DELIVERY_MESSAGE_THREAD_ID,
        reply_markup=buttons.NEW_DELIVERY(user_id, distance, maps_link)
    )
    # send message succes fuly delivery
    await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[lang], reply_markup=buttons.MENU[lang])
    await state.set_state(Delivery.attribution_send)

@dp.meage_handler(content_types=['location'], state=Delivery.location)
async def delivery_location(message: Message, state: FSMContext):
    await create_task(delivery_location_task(message, state))