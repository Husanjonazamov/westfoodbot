# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from asyncio import create_task
#
# # from recyclable.main_menu import main_menu
# from utils import texts, buttons
# from states import Delivery, FoodOrder
# from loader import dp
#
# from services.services import getUser, getBasketList, getCategorys
#
#
# async def set_phone_task(phone: str, message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#
#     # user ma'lumotlarin
#     user = getUser(user_id)
#     lang = user['lang']
#     data = await state.get_data()
#     add_note = data.get('add_note')
#     location_name = data.get('location_name')
#     basket = getBasketList(user_id)
#
#     await state.update_data(phone=phone)
#     # phone validator
#     if len(phone) > 8 and any(char.isdigit() for char in phone):
#         if lang == "uz":
#             await state.set_state(Delivery.attribution_send)
#             await message.answer(
#                 text=texts.USER_DELIVERY_ATTRIBUTION_UZ(
#                     basket=basket,
#                     phone=phone,
#                     add_note=add_note,
#                     location_name=location_name
#                 ),
#                 reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#             )
#         elif lang == "en":
#             await state.set_state(Delivery.attribution_send)
#             await message.answer(
#                 text=texts.USER_DELIVERY_ATTRIBUTION_EN(
#                     basket=basket,
#                     phone=phone,
#                     add_note=add_note,
#                     location_name=location_name
#                 ),
#                 reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#             )
#         else:
#             await state.set_state(Delivery.attribution_send)
#             await message.answer(
#                 text=texts.USER_DELIVERY_ATTRIBUTION_RU(
#                     basket=basket,
#                     phone=phone,
#                     add_note=add_note,
#                     location_name=location_name
#                 ),
#                 reply_markup=buttons.ORDER_ATTRIBUTION[lang]
#             )
#     else:
#         if lang == "uz":
#             await message.answer(texts.PHONE_NUMBER_LEN_RULE_UZ if len(phone) <= 8 else texts.PHONE_RULE_UZ)
#         elif lang == "en":
#             await message.answer(texts.PHONE_NUMBER_LEN_RULE_EN if len(phone) <= 8 else texts.PHONE_RULE_EN)
#         else:
#             await message.answer(texts.PHONE_NUMBER_LEN_RULE_RU if len(phone) <= 8 else texts.PHONE_RULE_RU)
#
#
# @dp.message_handler(state=Delivery.phone, content_types=['text'])
# async def phone_number_text(message: types.Message, state: FSMContext):
#     print("Message received:", message.text)  # Debugging uchun
#     if message.text in [buttons.DELIVERY_PHONE_BACK_UZ,
#                         buttons.DELIVERY_PHONE_BACK_RU,
#                         buttons.DELIVERY_PHONE_BACK_EN]:
#         print("Back button pressed:", message.text)  # Debugging uchun
#         user_id = message.from_user.id
#         user = getUser(user_id)
#         lang = user['lang']
#
#         print(await state.get_data())
#
#         await message.answer(text=texts.ORDER_LOCATION[lang], reply_markup=buttons.ORDER_LOCATION[lang])
#         await Delivery.location.set()
#     else:
#         print("Other button pressed:", message.text)  # Debugging uchun
#         create_task(set_phone_task(message.text, message, state))
#
#     # Har bir bosqichdan so'ng state holatini tekshiramiz
#     current_state = await state.get_state()
#     print("Current state:", current_state)
#
#
# @dp.message_handler(state=Delivery.phone, content_types=['contact'])
# async def phone_number_contact(message: types.Message, state: FSMContext):
#     print("Contact received:", message.contact.phone_number)  # Debugging uchun
#     phone = message.contact.phone_number
#     create_task(set_phone_task(phone, message, state))
#
#     # Har bir bosqichdan so'ng state holatini tekshiramiz
#     current_state = await state.get_state()
#     print("Current state:", current_state)
