from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from services.services import clearBasketAndSetRating, getUser
from utils import texts
from utils.constantas import ORDER_SEND_CHAT
# from ORDER_SEND_CHAT


async def handle_take_succes_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    message_id = data_split[0].replace("trash_take:", "")
    user_id = data_split[1].replace("user_id:", "")

    user = getUser(user_id)
    lang = user['lang']

    # clear basket and set rating
    clearBasketAndSetRating(user_id)

    await bot.send_message(
        chat_id=user_id,
        text=texts.THAKS_SERVICES[lang]
    )
    await bot.delete_message(chat_id=ORDER_SEND_CHAT, message_id=message_id)


@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("trash_take:"), state="*")
async def handle_take_succes(callbask_query: CallbackQuery, state: FSMContext):
    create_task(handle_take_succes_task(callbask_query, state))
