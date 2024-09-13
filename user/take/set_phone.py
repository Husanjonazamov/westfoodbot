# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from asyncio import create_task
#
# from services.services import getUser
# from states import  TakeAway
# from utils import texts, buttons
# from loader import dp
#
#
# async def set_phone_task(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#
#     user = getUser(user_id)
#     lang = user['lang']
#
#     if (lang == "uz"):
#         await state.update_data(phone=message.text)
#         # phone validator
#         if len(message.text) > 8:
#             if not ("0" in message.text or
#                     "1" in message.text or
#                     "2" in message.text or
#                     "3" in message.text or
#                     "4" in message.text or
#                     "5" in message.text or
#                     "6" in message.text or
#                     "7" in message.text or
#                     "8" in message.text or
#                     "9" in message.text):
#                 await message.answer(texts.phone_rule_uz)
#             else:
#                 await state.set_state(TakeAway.time)
#                 await message.answer(texts.take_time_uz, reply_markup=buttons.BACK_UZ)
#         else:
#             await message.answer(texts.phone_nomer_len_rule_uz)
#     elif (lang == "en"):
#         phone = message.text
#         await state.update_data(phone=message.text)
#         if len(message.text) > 8:
#             if not ("0" in message.text or
#                     "1" in message.text or
#                     "2" in message.text or
#                     "3" in message.text or
#                     "4" in message.text or
#                     "5" in message.text or
#                     "6" in message.text or
#                     "7" in message.text or
#                     "8" in message.text or
#                     "9" in message.text):
#                 await message.answer(texts.phone_rule_en)
#             else:
#                 await state.set_state(TakeAway.time)
#                 await message.answer(texts.take_time_en, reply_markup=buttons.BACK_EN)
#         else:
#             await message.answer(texts.phone_nomer_len_rule_en)
#     elif (lang == "ru"):
#         phone = message.text
#         await state.update_data(phone=message.text)
#         # phone validator
#         if len(message.text) > 8:
#             if not ("0" in message.text or
#                     "1" in message.text or
#                     "2" in message.text or
#                     "3" in message.text or
#                     "4" in message.text or
#                     "5" in message.text or
#                     "6" in message.text or
#                     "7" in message.text or
#                     "8" in message.text or
#                     "9" in message.text):
#                 await message.answer(texts.phone_rule_ru)
#             else:
#                 await state.set_state(TakeAway.time)
#                 await message.answer(texts.take_time_ru, reply_markup=buttons.BACK_RU)
#
#         else:
#             await message.answer(texts.phone_nomer_len_rule_ru)
#
#
# @dp.message_handler(state=TakeAway.phone, content_types=['text'])
# async def phone_number(message: types.Message, state: FSMContext):
#     create_task(set_phone_task(message, state))
