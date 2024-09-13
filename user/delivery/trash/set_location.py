# from aiogram.dispatcher.storage import FSMContext
# from aiogram.types import Message
# from loader import dp
# from asyncio import create_task
# from services.services import getUser
# from states import Delivery
# from utils import texts, buttons
# from utils.functions import get_location_name
# from translate import Translator

# async def delivery_location_task(message: Message, state: FSMContext):
#     # main ma'lumotlarni olish
#     user_id = message.from_user.id
#     user = getUser(user_id)
#     lang = user['lang']

#     lat = message.location.latitude
#     lon = message.location.longitude

#     translator = Translator(to_lang=lang)

#     location_name = get_location_name(lat, lon)

#     location_name_translate = translator.translate(location_name)

#     await state.update_data({
#         'location': {
#             'latitude': lat,
#             'longitude': lon
#         },
#         'location_name': location_name_translate,
#     })
#     print(f'{message.location} --------------')  # Debugging uchun
#     await message.answer(texts.USER_LOCATION[lang].format(location_name_translate), reply_markup=buttons.LOCATION_ORDER[lang])

#     # # send message successfully delivery
#     await state.set_state(Delivery.location_check)



# @dp.message_handler(content_types=['location'], state=Delivery.location)
# async def handle_location(message: Message, state: FSMContext):
#     print("Location received:")  # Debugging uchun
#     await create_task(delivery_location_task(message, state))



# @dp.message_handler(content_types=['text'], state=Delivery.location)
# async def handle_text(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#     user = getUser(user_id)
#     lang = user['lang']
#     print("Message received:", message.text)  # Debugging uchun
#     if message.text in [buttons.ORTGA_BUTTON_LOCATION_UZ, buttons.ORTGA_BUTTON_LOCATION_RU, buttons.ORTGA_BUTTON_LOCATION_EN]:
#         print("Back button pressed:", message.text)  # Debugging uchun
#         user_id = message.from_user.id
#         user = getUser(user_id)
#         lang = user['lang']
#         state_data = await state.get_data()
#         await message.answer(texts.DELEVERY_COMMENT_TEXT[lang], reply_markup=buttons.DELIVERY_SET_BUTTON[lang])
#         await Delivery.addComment.set()
#     elif message.text not in [buttons.ORTGA_BUTTON_LOCATION_UZ, buttons.ORTGA_BUTTON_LOCATION_RU, buttons.ORTGA_BUTTON_LOCATION_EN]:
#         await message.answer(texts.LOCATION_NOT_FOUND[lang], reply_markup=buttons.ORDER_LOCATION[lang])
#         await Delivery.location.set()

#     # Har bir bosqichdan so'ng state holatini tekshiramiz
#     current_state = await state.get_state()
#     print("Current state:", current_state)
