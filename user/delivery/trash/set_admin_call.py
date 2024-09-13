# from aiogram.dispatcher.storage import FSMContext
# from aiogram.types import Message
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from loader import dp
# from asyncio import create_task
# from aiogram.types import CallbackQuery

# from states import Delivery, FoodOrder
# from services.services import getBasketList, getUser, getCategorys
# from utils import texts, buttons


# async def add_task(message: Message, state: FSMContext):
#     user_id = message.from_user.id

#     # user ma'lumotlarin
#     user = getUser(user_id)
#     lang = user['lang']

#     await state.update_data(addnote=message.text)

#     basket = getBasketList(user_id)

#     if not basket:
#         await message.answer(text=texts.EMPTY_BASKET[lang])
#         return
#     # menu yuborish

#     await message.answer(texts.PHONE_DELIVERY[lang], reply_markup=buttons.DELIVERY_PHONE[lang])

#     await state.set_state(Delivery.phone)



# @dp.message_handler(state=Delivery.admin_call, content_types=['text'])
# async def phone_number(message: Message, state: FSMContext):
#     print("Message received:", message.text)  # Debugging uchun
#     if message.text in [buttons.ADMIN_MENU_UZ, buttons.ADMIN_MENU_RU, buttons.ADMIN_MENU_EN]:
#         print("Back button pressed:", message.text)  # Debugging uchun
#         user_id = message.from_user.id
#         user = getUser(user_id)
#         lang = user['lang']
#         state_data = await state.get_data()
#         category = getCategorys()
#         # categoryani yuborish
#         await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))
#         await FoodOrder.category.set()
#     elif message.text in [buttons.ADMIN_BACK_UZ, buttons.ADMIN_BACK_RU,
#                           buttons.ADMIN_BACK_EN]:
#         print("Back button pressed:", message.text)  # Debugging uchun
#         user_id = message.from_user.id
#         user = getUser(user_id)
#         lang = user['lang']
#         state_data = await state.get_data()
#         # categoryani yuborish
#         await message.answer(texts.DELEVERY_COMMENT_TEXT[lang], reply_markup=buttons.DELIVERY_SET_BUTTON[lang])
#         await Delivery.addComment.set()
#     else:
#         print("Other button pressed:", message.text)  # Debugging uchun
#         await create_task(add_task(message, state))

#     # Har bir bosqichdan so'ng state holatini tekshiramiz
#     current_state = await state.get_state()
#     print("Current state:", current_state)
