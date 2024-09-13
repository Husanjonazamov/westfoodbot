
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp
from asgiref.sync import sync_to_async

from services.services import createUserPhone
from states import Register
from bot.models import UserPhones
from utils import texts, buttons


async def _task(message: types.Message, state: FSMContext, phone_number: str):
    """
    Userni contact ma'lumotlarini olish va contact ma'lumotin olingandan
    so'ng userni 'fullname' statega o'tqazish
    """

    # userni contact ma'lumotlarini olish
    state_data = await state.get_data()
    lang = state_data['lang']

    # userdan fullnameini so'rash
    await message.answer(text=texts.FULLNAME[lang], reply_markup=buttons.REMOVE_BUTTON)

    # stateni yangilash, phoneni qo'shish
    await state.update_data({
        'phone': phone_number,
        'lang': lang
    })
    # UserPhone modeliga telefon raqamni saqlash

    # stateni fullnamega o'tqazish
    await Register.fullname.set()

@dp.message_handler(content_types=['contact'], state=Register.phone)
async def phone(message: types.Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number
    create_task(_task(message, state, phone_number))