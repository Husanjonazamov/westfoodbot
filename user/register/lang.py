
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from states import Register

from utils import buttons, texts



async def _task(message: types.Message, state: FSMContext):
    """
    Ro'yxatdan o'tmagan userni ro'yxatdan o'tqazishni boshlash va
    Bu yerda userni tili aniqlanadi
    """
    lang = message.text


    lang_codes = {
        buttons.LANGUAGES_UZ: 'uz',
        buttons.LANGUAGES_RU: 'ru',
        buttons.LANGUAGES_EN: 'en'
    }


    if not lang in lang_codes:
        """
        Agar user xato til kiritsa
        """
        await message.delete()
        return

    # til codeni olish
    lang = lang_codes[lang]

    # olingan til codeni statega joylash
    await state.set_data({
        'lang': lang
    })

    # userdan telefon raqamini yuborishni so'rash
    await message.answer(text=texts.PHONE[lang], reply_markup=buttons.PHONE[lang])

    # stateni telefon raqamiga o'tqazish
    await state.set_state(Register.phone)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Register.lang)
async def lang(message: types.Message, state: FSMContext):
    await create_task(_task(message, state))
