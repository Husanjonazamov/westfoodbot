from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import putUserLang
from states import UpdateRegisterLang
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from asgiref.sync import sync_to_async
from asgiref.sync import sync_to_async


async def lang_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # user ma'lumotlarin

    lang_codes = {
        buttons.LANGUAGES_UZ: 'uz',
        buttons.LANGUAGES_RU: 'ru',
        buttons.LANGUAGES_EN: 'en'
    }

    lang_new = message.text
    lang = lang_codes[lang_new]
    user = putUserLang(user_id, lang)
    # olingan til codeni statega joylash
    await state.set_data({
        'lang': lang
    })
    print(lang)
    await message.answer(text=texts.LANG_SWITCH[lang], reply_markup=buttons.MENU[lang])
    await state.finish()



@dp.message_handler(state=UpdateRegisterLang.lang)
async def lang(message: Message, state: FSMContext):
    create_task(lang_task(message, state))