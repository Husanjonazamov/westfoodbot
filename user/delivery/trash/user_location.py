# print("2. start order...")

# from aiogram import types
# from aiogram.dispatcher import FSMContext

# from loader import dp
# from bot.models import UserPhones
# from asyncio import create_task

# from services.services import getCategorys, getUser, getBasketList, getUserPhone
# from asgiref.sync import sync_to_async
# from states import Delivery
# from utils import buttons, texts



# async def _atask(message: types.Message, state: FSMContext):

#     user_id = message.from_user.id

#     # user ma'lumotlarin
#     user = getUser(user_id)
#     phone = user['phone']

#     lang = user['lang']
#     data = await state.get_data()
#     add_note = data.get('add_note')
#     location_name = data.get('location_name')
#     basket = getBasketList(user_id)




#     if lang == "uz":
#         await state.set_state(Delivery.attribution_send)
#         await message.answer(
#             text=texts.USER_DELIVERY_ATTRIBUTION_UZ(
#                 basket=basket,
#                 phone=phone,
#                 add_note=add_note,
#                 location_name=location_name
#             ),
#             reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#         )
#     elif lang == "en":
#         await state.set_state(Delivery.attribution_send)
#         await message.answer(
#             text=texts.USER_DELIVERY_ATTRIBUTION_EN(
#                 basket=basket,
#                 phone=phone,
#                 add_note=add_note,
#                 location_name=location_name
#             ),
#             reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#         )
#     else:
#         await state.set_state(Delivery.attribution_send)
#         await message.answer(
#             text=texts.USER_DELIVERY_ATTRIBUTION_RU(
#                 basket=basket,
#                 phone=phone,
#                 add_note=add_note,
#                 location_name=location_name
#             ),
#             reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#         )


#     await state.set_state(Delivery.attribution_send)



# @dp.message_handler(
#     lambda message: message.text.startswith((
#                         buttons.LOCATION_CHECK_UZ,
#                         buttons.LOCATION_CHECK_RU,
#                         buttons.LOCATION_CHECK_EN,)
#                         ),
#     state=Delivery.location_check)



# async def order(message: types.Message, state: FSMContext):
#     print("Message received:", message.text)  # Debugging uchun
#     await create_task(_atask(message, state))



# @dp.message_handler(content_types=['text'], state=Delivery.location_check)
# async def handle_text(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     user = getUser(user_id)
#     lang = user['lang']
#     if message.text in [buttons.ORDER_LOCATION_CHECK_BACK_UZ, buttons.ORDER_LOCATION_CHECK_BACK_RU, buttons.ORDER_LOCATION_CHECK_BACK_EN]:
#         print("Back button pressed:", message.text)  # Debugging uchun
#         user_id = message.from_user.id
#         user = getUser(user_id)
#         lang = user['lang']
#         state_data = await state.get_data()
#         await message.answer(text=texts.ORDER_LOCATION[lang], reply_markup=buttons.ORDER_LOCATION[lang])
#         await Delivery.location.set()
#     else:
#         await message.answer(texts.NOT_TEXT[lang])
#         print("Other button pressed:", message.text)  # Debugging uchun

#     # Har bir bosqichdan so'ng state holatini tekshiramiz
#     current_state = await state.get_state()
#     print("Current state:", current_state)
