# from aiogram.dispatcher.storage import FSMContext
#
# from loader import dp, bot
# from asyncio import create_task
# from aiogram.types import CallbackQuery
# from services.services import getUser
# from utils import texts, buttons
#
# async def handle_take_succes_task(call: CallbackQuery, state: FSMContext):
#     data_split = call.data.split('-')
#     user_id = data_split[1].replace("user_id:", "")
#     old_message_text = call.message.text
#
#     user = getUser(user_id)
#     lang = user['lang']
#
#     await bot.send_message(
#         chat_id=user_id,
#         text=texts.SUCCES_TAKE[lang]
#     )
#
#     await call.message.edit_text(
#         text=old_message_text + "\n\n" + "✅ Buyurtma tasdiqlandi",
#         reply_markup=buttons.TAKE_PREPARING_BUTTON(user_id)
#     )
#
#
# @dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("t_succes:"))
# async def handle_take_succes(callbask_query: CallbackQuery, state: FSMContext):
#     create_task(handle_take_succes_task(callbask_query, state))
