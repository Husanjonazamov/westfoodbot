from aiogram.types import Message
from asyncio import create_task

from loader import dp
from services.services import getUser
from utils import buttons, texts
from aiogram.dispatcher import FSMContext


async def info_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)

    # menu yuborish
    await message.answer(texts.INFO[lang], reply_markup=buttons.INFORMATION[lang])


@dp.message_handler(
    lambda message: message.text.startswith(buttons.MENU_INFO_UZ) or \
                    message.text.startswith(buttons.MENU_INFO_RU) or \
                    message.text.startswith(buttons.MENU_INFO_EN)
)
async def func(message: Message, state: FSMContext):
    await create_task(info_handler(message, state))
