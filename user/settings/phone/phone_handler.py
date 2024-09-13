from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import getUser
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from states import UpdateRegisterPhone


async def settings_answer_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    state_data = await state.get_data()
    user = getUser(user_id)
    lang = user['lang']
    
    # userdan fullnameini so'rash
    await message.answer(text=texts.PHONE[lang], reply_markup=buttons.ORTGA[lang])
    
    # stateni yangilash, phoneni qo'shish

    # stateni fullnamega o'tqazish
    await UpdateRegisterPhone.phone.set()


@dp.message_handler(
        lambda message: message.text.startswith(buttons.PHONE_SWITCH_UZ) or \
                message.text.startswith(buttons.PHONE_SWITCH_RU) or \
                    message.text.startswith(buttons.PHONE_SWITCH_EN)
        )
async def settings_answer(message: Message, state: FSMContext):
      await create_task(settings_answer_task(message, state))