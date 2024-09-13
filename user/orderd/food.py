from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from asyncio import create_task
from services.services import getCategorys, getFood, getUser
from states import FoodOrder
from user.orderd.start_order import order
from utils import buttons, texts

def format_price(price):
    return f"{price:,}".replace(',', ' ')

async def _task(message: types.Message, state: FSMContext):
    """
    Bitta maxsulotni ko'rish
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    food_name = message.text
    print(food_name)

    # maxsulotni olish
    food = getFood(food_name=food_name)

    if not food:
        await message.delete()
        return

    # maxsulotning file_id ni olish
    img_file_id = food['img_file_id']

    # Narxni formatlash
    food_price_formatted = format_price(food['price'])

    if lang == 'uz':
        food_description = food['description_uz']
        food_price = food_price_formatted
    elif lang == 'ru':
        food_description = food['description_ru']
        food_price = food_price_formatted
    else:
        food_description = food['description_en']
        food_price = food_price_formatted

    if lang == 'uz':
        if food_description:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_DESCRIPTION_UZ.format(
                    food_name,
                    food_price,
                    food_description,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])
        else:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_NOT_DESCRIPTION_UZ.format(
                    food_name,
                    food_price,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])
    elif lang == 'ru':
        if food_description:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_DESCRIPTION_RU.format(
                    food_name,
                    food_price,
                    food_description,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])
        else:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_NOT_DESCRIPTION_RU.format(
                    food_name,
                    food_price,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])
    else:
        if food_description:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_DESCRIPTION_EN.format(
                    food_name,
                    food_price,
                    food_description,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])
        else:
            await message.answer_photo(
                photo=img_file_id,
                caption=texts.FOOD_NOT_DESCRIPTION_EN.format(
                    food_name,
                    food_price,
                ),
                reply_markup=buttons.FOOD_RETRIVE[lang],
            )
            await message.answer(texts.FOOD_QUANTITY_REQUEST[lang])

    # user tanlagan maxsulotni statega joylash
    await state.update_data({
        'food_name': food_name
    })

    # stateni countga o'tqazish
    await FoodOrder.count.set()

@dp.message_handler(state=FoodOrder.food)
async def food(message: types.Message, state: FSMContext):
    if message.text in (buttons.FOOD_TEXT_BACK_UZ, buttons.FOOD_TEXT_BACK_RU, buttons.FOOD_TEXT_BACK_EN):
        print("Message received:", message.text)  # Debugging uchun

        print("Back button pressed:", message.text)  # Debugging uchun
        user_id = message.from_user.id
        user = getUser(user_id)
        lang = user['lang']
        category = getCategorys()

        await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
        await state.set_state(FoodOrder.category)
    else:
        create_task(_task(message, state))

    # Har bir bosqichdan so'ng state holatini tekshiramiz
    current_state = await state.get_state()
    print("food state:", current_state)

    print("food quantity State: ", await state.get_data())
