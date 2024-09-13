# from aiogram.dispatcher.storage import FSMContext
# from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
# from loader import dp
# from asyncio import create_task
# from aiogram import types
# from services.services import getBasketList, getUser
# from states import TakeAway
# from utils import texts, buttons
#
#
# async def take_task(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     user = getUser(user_id)
#     lang = user['lang']
#
#
#     basket = getBasketList(user_id)
#
#     if not basket:
#         await message.answer(text=texts.EMPTY_BASKET[lang])
#         return
#
#
#     phone_list_user_uz = ReplyKeyboardMarkup(
#         keyboard=[
#             # [
#             #     KeyboardButton(text=phone)
#             # ],
#             [
#                 KeyboardButton(text='🔙 Ortga')
#             ]
#         ],
#         resize_keyboard=True
#     )
#     phone_list_user_en = ReplyKeyboardMarkup(
#         keyboard=[
#             # [
#             #     KeyboardButton(text=user_phone.phone)
#             # ],
#             [
#                 KeyboardButton(text='🔙 Back')
#             ]
#         ],
#         resize_keyboard=True
#     )
#     phone_list_user_ru = ReplyKeyboardMarkup(
#         keyboard=[
#             # [
#             #     KeyboardButton(text=user_phone.phone)
#             # ],
#             [
#                 KeyboardButton(text='🔙 Назад')
#             ]
#         ],
#         resize_keyboard=True
#     )
#
#
#     if (lang== "uz"):
#         await message.answer(texts.TAKE_PHONE_UZ, reply_markup=phone_list_user_uz)
#     elif (lang== "en"):
#         await message.answer(texts.TAKE_PHONE_EN, reply_markup=phone_list_user_en)
#     elif (lang== "ru"):
#         await message.answer(texts.TAKE_PHONE_RU, reply_markup=phone_list_user_ru)
#
#     await TakeAway.phone.set()
#
# @dp.message_handler(
#     lambda message: message.text.startswith((
#                         buttons.TAKE_UZ,
#                         buttons.TAKE_RU,
#                         buttons.TAKE_EN,)
#                         ),
#     state='*')
# async def take_food(callbask_query: CallbackQuery, state: FSMContext):
#     create_task(take_task(callbask_query, state))