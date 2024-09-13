from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from loader import dp
from asyncio import create_task
from services.services import getUser
from states import FoodOrder, Delivery
from user.menu import MainMenu
from utils import texts, buttons
from utils.restoran_location import calculate_distance, MAX_DELIVERY_DISTANCE_KM, RESTAURANT_LOCATION
from utils.functions import get_location_name
from translate import Translator





async def delivery_location_task(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    

    # main ma'lumotlarni olish
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['lang']

    translator = Translator(to_lang=lang)

    location_name = get_location_name(lat, lon)
    location_name_translate = translator.translate(location_name)

    distance = calculate_distance(lat, lon, RESTAURANT_LOCATION['latitude'], RESTAURANT_LOCATION['longitude'])

    if distance > MAX_DELIVERY_DISTANCE_KM:
        await message.answer(texts.LOCATION_LONG[lang])
        await state.set_state(FoodOrder.location)
        return

    await state.update_data({
        'location': {
            'latitude': lat,
            'longitude': lon
        },
        'location_name': location_name_translate,
    })

    await message.answer(texts.USER_LOCATION[lang].format(location_name_translate), reply_markup=buttons.LOCATION_ORDER[lang])

    # FoodOrder.location_check holatiga o'tish
    await FoodOrder.location_check.set()
    print("User location State: ", await state.get_data())



@dp.message_handler(content_types=['location'], state=FoodOrder.location)
async def delivery_location(message: types.Message, state: FSMContext):
    await create_task(delivery_location_task(message, state))




