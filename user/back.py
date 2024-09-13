
print("1. Init back...")

from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from states import Register

from user.menu import MainMenu
from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    """

    # user id
    user_id = message.from_user.id

    current_state = await state.get_state()
    print(current_state)
    print(type(current_state))

    await MainMenu(message, state)

@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.ORTGA_BUTTON_UZ,
            buttons.ORTGA_BUTTON_RU,
            buttons.ORTGA_BUTTON_EN,
        )),
        state='*')
async def back(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
