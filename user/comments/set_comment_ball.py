from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from services.services import getUser
from utils import buttons
from aiogram import Bot
from utils import texts
from states import Comments
from asyncio import create_task
from utils.constantas import COMMENT_SEND_ID, COMMENT_MESSAGE_THREAD_ID


async def set_comment_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)


    

    await state.update_data(comment_at=message.text)
    data = await state.get_data()
    print(message.text)
    comment = message.text
    await bot.send_message(
        chat_id=COMMENT_SEND_ID,
        text=texts.NEW_COMMENT(
            comment=comment,
        ),
        reply_to_message_id=COMMENT_MESSAGE_THREAD_ID
    )
    await message.answer(texts.COMMENT_RECEPTION[lang], reply_markup=buttons.ORTGA[lang])
    await state.finish()
    # menu yuborish


@dp.message_handler(content_types=['text'], state=Comments.commen_ball)
async def comment(message: Message, state: FSMContext):
    create_task(set_comment_task(message, state))