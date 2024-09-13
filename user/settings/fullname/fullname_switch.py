from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import putUserFullname
from states import UpdateRegisterFullname
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from asgiref.sync import sync_to_async



async def lang_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # user ma'lumotlarin

    fullname = message.text
    # olingan til codeni statega joylash
    await state.set_data({
        'fullname': fullname
    })
    state_data = await state.get_data()
    phone = state_data['fullname']
    user = putUserFullname(user_id, fullname)
    lang = user['lang']
    await message.answer(text=texts.FULLANAME_SWITCH[lang], reply_markup=buttons.MENU[lang])

    await state.finish()


@dp.message_handler(state=UpdateRegisterFullname.fullname)
async def lang(message: Message, state: FSMContext):
    create_task(lang_task(message, state))