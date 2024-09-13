# from aiogram.dispatcher.storage import FSMContext
# from aiogram.types import Message
# from loader import dp, bot
# from asyncio import create_task
#
# from services.services import getBasketList, getUser
# from utils import buttons, texts
# from utils.constantas import ORDER_SEND_CHAT, ORDER_TAKE_MESSAGE_THREAD_ID
# from states import TakeAway
#
#
# async def time_task(message: Message, state: FSMContext):
#     user_id = message.from_user.id
#
#     await state.update_data(time=message.text)
#
#     user = getUser(user_id)
#     lang = user['lang']
#     fullname = user['fullname']
#
#     data = await state.get_data()
#     basket = getBasketList(user_id)
#
#     if (lang == "uz"):
#         await state.update_data(time=message.text)
#         # phone validator
#         if len(message.text):
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
#                 await message.answer(texts.time_rule_uz)
#             else:
#                 await state.finish()
#                 await bot.send_message(
#                         chat_id=ORDER_SEND_CHAT,
#                         text=texts.NEW_TAKE(
#                             basket=basket, time=data['time'], phone=data['phone'],
#                             )+ f"\n👤 Mijozning ismi: {fullname}",
#                         reply_to_message_id=ORDER_TAKE_MESSAGE_THREAD_ID,
#                         reply_markup=buttons.NEW_TAKE(user_id)
#                     )
#
#                 await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[lang], reply_markup=buttons.ORTGA[lang])
#
#     elif (lang == "en"):
#         await state.update_data(time=message.text)
#         # phone validator
#         if len(message.text):
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
#                 await message.answer(texts.time_rule_en)
#             else:
#                 await state.finish()
#                 await bot.send_message(
#                         chat_id=ORDER_SEND_CHAT,
#                         text=texts.NEW_TAKE(
#                             basket=basket, time=data['time'], phone=data['phone']
#                             ) + f"\n👤 Mijozning ismi: {fullname}",
#                         reply_to_message_id=ORDER_TAKE_MESSAGE_THREAD_ID,
#                         reply_markup=buttons.NEW_TAKE(user_id)
#                     )
#                 await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[lang], reply_markup=buttons.ORTGA[lang])
#     else:
#         await state.update_data(time=message.text)
#         # phone validator
#         if len(message.text):
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
#                 await message.answer(texts.time_rule_ru)
#             else:
#                 await state.finish()
#                 await bot.send_message(
#                         chat_id=ORDER_SEND_CHAT,
#                         text=texts.NEW_TAKE(
#                             basket=basket, time=data['time'], phone=data['phone']
#                             )+ f"\n👤 Mijozning ismi: {fullname}",
#                         reply_to_message_id=ORDER_TAKE_MESSAGE_THREAD_ID,
#                         reply_markup=buttons.NEW_TAKE(user_id)
#                     )
#                 await message.answer(texts.ORDER_SUCCES_SEND_ADMIN[lang], reply_markup=buttons.ORTGA[lang])
#     await state.finish()
# @dp.message_handler(content_types=['text'], state=TakeAway.time)
# async def time_answer(message: Message, state: FSMContext):
#     await create_task(time_task(message, state))