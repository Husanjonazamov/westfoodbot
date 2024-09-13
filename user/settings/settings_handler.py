from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import getUser
from utils import buttons, texts
from asyncio import create_task
from loader import dp



async def settings_answer_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)

    # menu yuborish
    await message.answer(texts.SETTINGS_TEXT[lang], parse_mode='HTML', reply_markup=buttons.SETTINGS_MENYU[lang])

@dp.message_handler(
        lambda message: message.text.startswith(buttons.MENU_SETTINGS_UZ) or \
                message.text.startswith(buttons.MENU_SETTINGS_RU) or \
                    message.text.startswith(buttons.MENU_SETTINGS_EN)
        )
async def settings_answer(message: Message, state: FSMContext):
      await create_task(settings_answer_task(message, state))