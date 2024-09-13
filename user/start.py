from aiogram import types
from aiogram.dispatcher import FSMContext

from user.menu import MainMenu
from services.services import getUser
from loader import dp

from asyncio import create_task

from states import Register

from utils import buttons, texts


async def send_welcome_task(message: types.Message, state: FSMContext):
    print("👆 action: start -> send_welcome_task")
    """
    /start, /help commandalari uchun. Botga birichi kirgan userni anilash
    va uni ro'yxatdan o'rtkazishga jo'natish yoki ro'yxatdan  o'tgan userni
    asosiy menuga o'tqazish
    """

    # user id
    user_id = message.from_user.id


    # user
    user = getUser(user_id)

    if not user:
        """
        Agar user ro'yxatdan o'tmagan bo'lsa
        uni ro'yxatdan o'tqaishga jo'natish
        """
        await message.answer(text=texts.LANGUAGES, reply_markup=buttons.LANGUAGES)
        await Register.lang.set()
        return

    await MainMenu(message=message, state=state)

@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    create_task(send_welcome_task(message, state))



@dp.message_handler(state='*', content_types=['photo'])
async def send_welcome(message: types.Message, state: FSMContext):
    if message.photo:
        file_id = message.photo[-1].file_id
        await message.answer(file_id)
