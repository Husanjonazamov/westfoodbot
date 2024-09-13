from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import getUser
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from states import UpdateRegisterLang


async def settings_answer_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)

    # menu yuborish
    await message.answer(texts.LANGUAGES, parse_mode='HTML', reply_markup=buttons.LANGUAGES)
    await state.set_state(UpdateRegisterLang.lang)

@dp.message_handler(
        lambda message: message.text.startswith(buttons.TIL_SOZLAMALARI_BUTTON_UZ) or \
                message.text.startswith(buttons.TIL_SOZLAMALARI_BUTTON_RU) or \
                    message.text.startswith(buttons.TIL_SOZLAMALARI_BUTTON_EN)
        )
async def settings_answer(message: Message, state: FSMContext):
      await create_task(settings_answer_task(message, state))