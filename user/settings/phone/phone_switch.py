from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import putUserPhone
from states import UpdateRegisterPhone
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from asgiref.sync import sync_to_async



async def lang_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone = message.text
    user = putUserPhone(user_id, phone)
    lang = user['lang']
    if len(message.text) > 8:
        if not ("0" in message.text or
                "1" in message.text or
                "2" in message.text or
                "3" in message.text or
                "4" in message.text or  
                "5" in message.text or
                "6" in message.text or
                "7" in message.text or
                "8" in message.text or
                "9" in message.text):
            await message.answer(texts.time_e[lang])
        else:
            # user ma'lumotlarin
            print(lang)
            # olingan til codeni statega joylash
            await state.set_data({
                'phone': phone
            })
            state_data = await state.get_data()
            phone = state_data['phone']
            await message.answer(text=texts.PHONE_SWITCH[lang], reply_markup=buttons.MENU[lang])

            await state.finish()
    else:
        await message.answer(texts.PHONE_SWITCH_E[lang])


@dp.message_handler(state=UpdateRegisterPhone.phone)
async def lang(message: Message, state: FSMContext):
    create_task(lang_task(message, state))