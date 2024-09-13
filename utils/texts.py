ORDER_ALREADY_SENT = {
    'uz': "Sizning buyurtmangiz allaqachon adminga yuborilgan, admin tez orada javob beradi.",
    'ru': "Ваш заказ уже отправлен администратору, администратор скоро ответит.",
    'en': "Your order has already been sent to the admin, the admin will respond shortly."
}



USER_BASKET_TZ_UZ = \
"""
*«❌ Maxsulot nomi»* - savatdan o'chirish
 *🆑 Savatni tozalash»* - savatni butunlay bo'shatish
"""


USER_BASKET_TZ_RU = \
"""
*«❌ Наименование »* - удалить одну позицию
 *«🆑 Очистка корзины»* - полная очистка корзины
"""

USER_BASKET_TZ_EN = \
"""
*«❌ Name »* - delete one position
 *«🆑 Cleaning the basket»* - Full wipe of basket
"""



USER_BASKET_TZ = {
    'uz': USER_BASKET_TZ_UZ,
    'ru': USER_BASKET_TZ_RU,
    'en': USER_BASKET_TZ_EN,
}



FOOD_QUANTITY_REQUEST = {
    'uz': "Miqdorini tanlang yoki kiriting:",
    'ru': "Выберите или введите количество:",
    'en': "Choose or enter the amount:",
}



COLOSE_RESTORAN_UZ = \
"""
Afsuski hozircha restoranimiz yopiq.
"""


COLOSE_RESTORAN_RU = \
"""
Безоговорочно for now, our restaurant is closed.
"""


COLOSE_RESTORAN_EN = \
"""
Unfortunately for now, our restaurant is closed
"""


COLOSE_RESTORAN = {
    'uz': COLOSE_RESTORAN_UZ,
    'ru': COLOSE_RESTORAN_RU,
    'en': COLOSE_RESTORAN_EN,
}



NOT_TEXT = {
    'uz': "Iltimos pastdagilardan birini yuboring",
    'ru': "Пожалуйста, отправьте один из следующих",
    'en': "Please send one of the bottom",
}



LOCATION_NOT_FOUND = {
    'uz': "Kechirasiz sizning manzilingizni aniqlay olmadik\nQayta urinib ko'rin.",
    'ru': 'Извините, мы не смогли определить ваш адрес\nпробовать еще раз.',
    'en': "Sorry we couldn't identify your location\nry.",
}




SUCCES_ADD_UZ = """
<b>
Sizning buyurtmangiz qabul qilindi
</b>
"""
SUCCES_ADD_EN = """
<b>
Your order has been received
</b>
"""

SUCCES_ADD_RU = """
<b>
Ваш заказ принят
</b>
"""

SUCCES_ADD = {
    'uz': SUCCES_ADD_UZ,
    'ru': SUCCES_ADD_RU,
    'en': SUCCES_ADD_EN,
}





SUCCES_PAYMENT_UZ = """
<b>
To'lovni amalga oshirishingiz mumkin.
</b>
"""
SUCCES_PAYMENT_EN = """
<b>
You can make a payment
</b>
"""

SUCCES_PAYMENT_RU = """
<b>
Вы можете произвести оплату
</b>
"""

SUCCES_PAYMENT = {
    'uz': SUCCES_PAYMENT_UZ,
    'ru': SUCCES_PAYMENT_RU,
    'en': SUCCES_PAYMENT_EN,
}



























FOOD_NOT_DESCRIPTION_UZ = \
"""
<b>
{}\n

Narxi: {} so'm\n

</b>
"""

FOOD_NOT_DESCRIPTION_RU = \
"""
<b>
{}\n

Стоимость: {} Cyм\n

</b>
"""

FOOD_NOT_DESCRIPTION_EN = \
"""
<b>
{}\n

Price: {} soum\n

</b>
"""



LOCATION_LONG_UZ = \
"""
Yetkaib berish zonasidan tashqarida
"""

LOCATION_LONG_RU = \
"""
Вне зоны доставки
"""

LOCATION_LONG_EN = \
"""
Out of reach zone
"""


LOCATION_LONG = {
    'uz': LOCATION_LONG_UZ,
    'ru': LOCATION_LONG_RU,
    'en': LOCATION_LONG_EN,
}




PAYMENT_UZ = \
"""
Buyurtmangiz uchun to'lov turini tanlang
"""

PAYMENT_EN = \
"""
Choose the type of payment for your order
"""


PAYMENT_RU = \
"""
Выберите тип оплаты для вашего заказа
"""


PAYMENT = {
    'uz': PAYMENT_UZ,
    'en': PAYMENT_EN,
    'ru': PAYMENT_RU,
}





ADMIN_CALL_UZ = \
"""
Buyurtmangizni tasdiqlash uchun operator qo'ng'irog'i kerakmi?
"""

ADMIN_CALL_RU = \
"""
Вам нужен звонок оператора для подтверждения вашего заказа?
"""

ADMIN_CALL_EN = \
"""
Do you need an operator call to confirm your order?
"""


ADMIN_CALL_TEXT = {
    'uz': ADMIN_CALL_UZ,
    'ru': ADMIN_CALL_RU,
    'en': ADMIN_CALL_EN,
}


DELEVERY_COMMENT_UZ = \
"""
Buyurtmaga izoh qoldiring
"""

DELEVERY_COMMENT_RU = \
"""
Оставьте комментарий к заказу
"""

DELEVERY_COMMENT_EN = \
"""
Leave a comment on the order
"""

DELEVERY_COMMENT_TEXT = {
    'uz': DELEVERY_COMMENT_UZ,
    'ru': DELEVERY_COMMENT_RU,
    'en': DELEVERY_COMMENT_EN,
}




def format_price(price):
    return f"{price:,}".replace(',', ' ')



def USER_DELIVERY_ATTRIBUTION_UZ(**kwargs):
    new_order_message_text = ""
    total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi
    new_order_message_text += f"\n\n"

    new_order_message_text += f"Buyurtma turi: 🚖 Yetkazib berish\n"
    new_order_message_text += f"Telefon: <a href='{kwargs['phone']}\n'>{kwargs['phone']}</a>\n"
    new_order_message_text += f"Ism: {kwargs['fullname']}\n"
    new_order_message_text += f"Izohlar: {kwargs['add_note']}\n"
    new_order_message_text += f"To'lov turi: {kwargs['payment_type']}\n"
    new_order_message_text += f"Manzil: {kwargs['location_name']}\n\n"
    for i in kwargs['basket']:
        item_name = i['food']['name_uz']
        item_count = i['count']
        item_price = i['food']['price']
        item_total = item_count * item_price

        formatted_item_price = format_price(item_price)
        formatted_item_total = format_price(item_total)

        new_order_message_text += f"\n{item_name}\n"
        new_order_message_text += f"{item_count} X {formatted_item_price} so'm = {formatted_item_total} so'm\n"

        total_price += item_total  

    formatted_total_price = format_price(total_price)
    new_order_message_text += f"\nUmumiy narx: {formatted_total_price} so'm\n"

    return new_order_message_text




def format_price(price):
    return f"{price:,}".replace(',', ' ')

def USER_DELIVERY_ATTRIBUTION_RU(**kwargs):
    new_order_message_text = ""
    total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi
    new_order_message_text += f"\n\n"

    new_order_message_text += f"Тип заказа: 🚖 Доставка\n"
    new_order_message_text += f"Телефон: <a href='{kwargs['phone']}\n'>{kwargs['phone']}</a>\n"
    new_order_message_text += f"имя: {kwargs['fullname']}\n"
    new_order_message_text += f"Примечания: {kwargs['add_note']}\n"
    new_order_message_text += f"Тип оплаты: {kwargs['payment_type']}\n"
    new_order_message_text += f"Адрес: {kwargs['location_name']}\n\n"

    for i in kwargs['basket']:
        item_name = i['food']['name_uz']
        item_count = i['count']
        item_price = i['food']['price']
        item_total = item_count * item_price

        formatted_item_price = format_price(item_price)
        formatted_item_total = format_price(item_total)

        new_order_message_text += f"\n{item_name}\n"
        new_order_message_text += f"{item_count} X {formatted_item_price} Сум = {formatted_item_total} Сум\n"

        total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

    formatted_total_price = format_price(total_price)
    # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
    new_order_message_text += f"\nОбщая стоимость: {formatted_total_price} Сум\n"

    return new_order_message_text




def format_price(price):
    return f"{price:,}".replace(',', ' ')

def USER_DELIVERY_ATTRIBUTION_EN(**kwargs):
    new_order_message_text = ""
    total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi
    new_order_message_text += f"\n\n"

    new_order_message_text += f"Order Type: 🚖 Delivery\n"
    new_order_message_text += f"Phone: <a href='{kwargs['phone']}\n'>{kwargs['phone']}</a>\n"
    new_order_message_text += f"Name: {kwargs['fullname']}\n"
    new_order_message_text += f"Notes: {kwargs['add_note']}\n"
    new_order_message_text += f"Type of payment: {kwargs['payment_type']}\n"
    new_order_message_text += f"Location: {kwargs['location_name']}\n\n"

    for i in kwargs['basket']:
        item_name = i['food']['name_uz']
        item_count = i['count']
        item_price = i['food']['price']
        item_total = item_count * item_price

        formatted_item_price = format_price(item_price)
        formatted_item_total = format_price(item_total)

        new_order_message_text += f"\n{item_name}\n"
        new_order_message_text += f"{item_count} X {formatted_item_price} Soum = {formatted_item_total} Soum\n"

        total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

    formatted_total_price = format_price(total_price)
    # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
    new_order_message_text += f"\nTotal price: {formatted_total_price} Soum\n"

    return new_order_message_text





ORDER_OTMEN_UZ = \
"""
Buyurtmangiz uchun to'lov turini tanlang
"""

ORDER_OTMEN_RU = \
"""
Выберите тип оплаты для вашего заказа
"""

ORDER_OTMEN_EN = \
"""
Choose the type of payment for your order
"""


ORDER_OTMEN = {
    'uz': ORDER_OTMEN_UZ,
    'ru': ORDER_OTMEN_RU,
    'en': ORDER_OTMEN_EN,
}





FOOD_DESCRIPTION_UZ = \
"""
<b>
{}\n

Narxi: {} so'm\n

{}\n
</b>
"""

FOOD_DESCRIPTION_RU = \
"""
<b>
{}\n

Стоимость: {} Cyм\n

{}\n
</b>
"""

FOOD_DESCRIPTION_EN = \
"""
<b>
{}\n

Price: {} soum\n

{}\n
</b>
"""

CLEAR_BASKET = {
    'uz': "<b>Savatchangiz tozalandi</b>",
    'ru': "<b>Ваша корзина очищена</b>",
    'en': "<b>Your basket has been cleared</b>",
}


MENU_UZ = """
<b>
Juda yaxshi birgalikda buyurtma beramizmi? 😃
</b>
"""

MENU_RU = """
<b>
Отлично! Оформим заказ вместе? 😃
</b>
"""

MENU_EN = """
<b>
Do we order very well together? 😃
</b>
"""


MENU = {
    'uz': MENU_UZ,
    'ru': MENU_RU,
    'en': MENU_EN,
}

LANGUAGES = """
<b>
Здравствуйте! Давайте для начала выберем язык обслуживания!

Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.

Hi! Let's first we choose language of serving!
</b>
"""


PHONE_UZ = """
<b>
📱 Telefon raqamingiz qanday? Telefon raqamingizni jo'natish uchun, quyidagi
"📱 Raqamni jo'natish" tugmasini bosing.
</b>
"""

PHONE_RU = """
<b>
📱 Какой у вас номер телефона? Чтобы отправить свой номер телефона, выполните следующие действия
Нажмите"📱 Отправить номер".
</b>
"""

PHONE_EN = """
<b>
📱 What is your phone number? To send your phone number, the following
Click " Send number📱".
</b>
"""
PHONE = {
    'uz': PHONE_UZ,
    'ru': PHONE_RU,
    'en': PHONE_EN,
}

FULLNAME_UZ = """
<b>
Ismingizni kiriting
</b>
"""

FULLNAME_RU = """
<b>
Введите свое имя
</b>
"""

FULLNAME_EN = """
<b>
Enter your name
</b>
"""

FULLNAME = {
    'uz': FULLNAME_UZ,
    'ru': FULLNAME_RU,
    'en': FULLNAME_EN,

}

FULLNAME_ERROR_UZ = """
<b>
Ismingizni to'g'ri kiriting
Misol uchun: 'Ibrohimjon'
</b>
"""

FULLNAME_ERROR_RU = """
<b>
Введите свое имя правильно
Например: "Ibrohimjon"
</b>
"""

FULLNAME_ERROR_EN = """
<b>
Enter your name correctly
For example: 'Ibrohimjon'
</b>
"""

FULLNAME_ERROR = {
    'uz': FULLNAME_ERROR_UZ,
    'ru': FULLNAME_ERROR_RU,
    'en': FULLNAME_ERROR_EN,
}


COMMENT_BALL_UZ = \
"""
West restoranini tanlaganingiz uchun rahmat.
Agar siz bizning xizmat sifatimizni yaxshilashimizga yordam bersangiz hursand bo'lardi.
Buning uchun 5 bal tizim asosida baholang
"""

COMMENT_BALL_RU = \
"""
Спасибо, что выбрали ресторан West.
Был бы рад, если бы вы помогли нам улучшить качество нашего обслуживания.
Для этого оцените по 5-балльной системе
"""

COMMENT_BALL_EN = \
"""
Thank you for choosing the West restaurant.
It would be nice if you helped us improve our quality of Service.
To do this, evaluate 5 points based on the system
"""


COMMENT_UZ = \
"""
O'z fikringizni qoldiring
"""

COMMENT_RU = \
"""
Оставь свой комментарий
"""

COMMENT_EN = \
"""
Leave your opinion
"""


COMMENT_RECEPTION_UZ = \
"""
Fikringiz uchun rahmat
"""

COMMENT_RECEPTION_RU = \
"""
Cпасибо вам за ваш отзыв
"""

COMMENT_RECEPTION_EN = \
"""
Thank you for your feedback
"""

COMMENT_RECEPTION = {
    'uz': COMMENT_RECEPTION_UZ,
    'ru': COMMENT_RECEPTION_RU,
    'en': COMMENT_RECEPTION_EN,
}



REGISTER_SUCCESS_UZ = """
<b>
Ro'yxatdan o'tdingiz
</b>
"""

REGISTER_SUCCESS_RU = """
<b>
Вы зарегистрировались
</b>
"""

REGISTER_SUCCESS_EN = """
<b>
Registered
</b>
"""


REGISTER_SUCCESS = {
    'uz': REGISTER_SUCCESS_UZ,
    'ru': REGISTER_SUCCESS_RU,
    'en': REGISTER_SUCCESS_EN,
}


CONTACT_UZ = \
"""
Agar sizda savollar bo'lsa bizga telefon qilishingiz mumkin:
93-887-00-00
"""

CONTACT_RU = \
"""
Вы можете позвонить нам, если у вас есть вопросы:
93-887-00-00
"""

CONTACT_EN = \
"""
To contact us\n
+998-93-887-00-00
"""


CONTACT = {
    'uz': CONTACT_UZ,
    'ru': CONTACT_RU,
    'en': CONTACT_EN,
}


INFO_UZ = \
"""
Milliondan ortiq mijozlar tashrif buyurgan!

West Restorani haqida qisqacha,west restorani 2022 yildan o'z faoliyatini boshlagan bo'lib, shu vaqt ichida milliondan ortiq tashrif buyuruvchilarga xizmat ko'rsatishga muvaffaq bo'ldi va nafaqat poytaxt aholisi, balki uning mehmonlari uchun ham diqqatga sazovor markazga aylandi!
West restoraning Manzili  Toshkent, Mirobod ko'chasi 1-etaj.


🕰 Ish soatlari

Dushanba: 10:00 – 00:00
Seshanba: 10:00 – 00:00
Chorshanba: 10:00 – 00:00
Payshanba: 10:00 – 00:00
Juma: 10:00 – 00:00
Shanba: 10:00 – 00:00
Yakshanba: 10:00 – 00:00



📝 O'ziga xos jihatlari!

🚗 Taomni tez va sifatli yetkazib berish
✅ Hamyonbop va sifatli taomlar!

Aniqroq ma'lumot va Manzilni ko'rish uchun pastdagi Manzilni ko'rish tugmasini bosing!

📞 Biz bilan bog'lanish uchun +998938870000
"""


INFO_RU = \
"""
Посетили более миллиона клиентов!

Вкратце о ресторане West ресторан west начал свою деятельность с 2022 года,за это время успел обслужить более миллиона посетителей и стал изюминкой не только для жителей столицы, но и для ее гостей!
Адрес ресторана West: Ташкент, ул. Мирабад, 1 этаж.


♦ Часы работы

Понедельник: 10:00 – 00:00
Вторник: 10:00 – 00:00
Среда: 10:00 – 00:00
Четверг: 10:00 – 00:00
Пятница: 10:00 – 00:00
Суббота: 10:00 – 00:00
Воскресенье: 10:00 – 00:00



Особенности работы!

♦ Быстрая и качественная доставка еды
♦ Доступная и качественная еда!

Нажмите кнопку "Просмотреть местоположение" ниже, чтобы увидеть более точную информацию и местоположение!

📞 +998938870000, чтобы связаться с нами
"""



INFO_EN = \
"""
More than a million customers have visited!

Briefly about the West restaurant, the West restaurant began its activities from 2022, during which time it managed to serve more than a million visitors and became a center of attraction not only for residents of the capital, but also for its guests!
The address of the West restaurant is Tashkent, mirabad Street 1 floor.


🕰 Working hours

Monday: 10:00 – 00:00
Tuesday: 10:00 – 00:00
Wednesday: 10:00 – 00:00
Thursday: 10:00 – 00:00
Friday: 10:00 – 00:00
Saturday: 10:00 – 00:00
Sunday: 10:00 – 00:00



📝 Specific aspects!

🚗 Fast and high quality food delivery
✅ Affordable and quality dishes!

Click the view address button at the bottom to see more specific information and address!

📞 To contact us +998938870000
"""


INFO = {
    'uz': INFO_UZ,
    'ru': INFO_RU,
    'en': INFO_EN,

}



lang_switch_handler_uz = \
"""
✅ Til muffaqiyatli almashtirildi
"""

lang_switch_handler_en = \
"""
✅ Language muffled replaced
"""

lang_switch_handler_ru = \
"""
✅ Язык успешно заменен
"""

LANG_SWITCH = {
    'uz':lang_switch_handler_uz,
    'en':lang_switch_handler_en,
    'ru':lang_switch_handler_ru,
}



phone_switch_handler_uz = \
"""
✅ Telefon raqam muffaqiyatli almashtirildi
"""

phone_switch_handler_en = \
"""
✅ Telefon number muffled replaced
"""

phone_switch_handler_ru = \
"""
✅ Телефон номер успешно заменен
"""


PHONE_SWITCH = {
    'uz':phone_switch_handler_uz,
    'en':phone_switch_handler_en,
    'ru':phone_switch_handler_ru,
}


fullname_switch_uz = \
"""
✅ Ism muffaqiyatli almashtirildi
"""

fullname_switch_ru = \
"""
✅ Имя успешно заменено
"""

fullname_switch_en = \
"""
✅ Name muffled replaced
"""

FULLANAME_SWITCH = {
    'uz':fullname_switch_uz,
    'en':fullname_switch_en,
    'ru':fullname_switch_ru,
}


ORDER_UZ = """
<b>
Nimadan boshlaymiz?
</b>
"""

ORDER_RU = """
<b>
С чего начнем?
</b>
"""

ORDER_EN = """
<b>
Where do we start?
</b>
"""
ORDER = {
    'uz': ORDER_UZ,
    'ru': ORDER_RU,
    'en': ORDER_EN,
}



ORDER_RESET = {
    'uz': "Davom etamizmi? 😉",
    'ru': "Продолжим? 😉",
    'en': "Let's proceed? 😉",
}






ORDER_LOCATION_UZ = \
"""
Buyurtmangizni qayerga yetkazib berish kerak 🚙?
"""

ORDER_LOCATION_RU = \
"""
Куда нужно доставить ваш заказ 🚙?
"""

ORDER_LOCATION_EN = \
"""
Where to deliver your order 🚙?
"""

ORDER_LOCATION = {
    'uz': ORDER_LOCATION_UZ,
    'ru': ORDER_LOCATION_RU,
    'en': ORDER_LOCATION_EN,
}


USER_LOCATION_UZ = \
"""
Sizning manzilingiz: {}
Joylashuvni tasdiqlang.
"""


USER_LOCATION_EN = \
"""
Your address: {}

Confirm the location.
"""


USER_LOCATION_RU = \
"""
Ваш адрес: {}

Подтвердите местоположение.
"""



USER_LOCATION = {
    'uz': USER_LOCATION_UZ,
    'ru': USER_LOCATION_RU,
    'en': USER_LOCATION_EN,
}



PHONE_RULE_UZ = \
"""
Telefon raqam sonlardan iborat bo'lishi kerak
"""

PHONE_RULE_RU = \
"""
Телефон номер должен состоять из цифр
"""

PHONE_RULE_EN = \
"""
The phone number must consist of numbers
"""

FOODS_UZ = """
<b>
Maxsulotni tanlang
</b>
"""

FOODS_RU = """
<b>
Выберите продукт
</b>
"""

FOODS_EN = """
<b>
Choose a product
</b>
"""

FOODS = {
    'uz': FOODS_UZ,
    'ru': FOODS_RU,
    'en': FOODS_EN
}


LOCATION_INFO = \
"""
https://yandex.uz/maps/10335/tashkent/house/YkAYdAFoT0QCQFprfX54dnpgZA==/?ll=69.268648%2C41.297337&z=19.22
"""

LOCATION_UZ = """
Manzilni kiriting
"""

LOCATION_RU = """
Введите адрес
"""

LOCATION_EN = """
Enter address
"""


PHONE_NUMBER_LEN_RULE_UZ = """
📞 Telifon raqam eng kamida 9 ta sondan iborat bo'lish kerak❌
"""

PHONE_NUMBER_LEN_RULE_RU = """
📞 Телефон номер должен состоять как минимум из 9 цифр❌
"""

PHONE_NUMBER_LEN_RULE_EN = """
📞 Telifon number must consist of at least 9 numbers ❌
"""

DELIVER_SEND = """
<b>
🛵 Qabul Qilingan buyurtma

+998{}

</b>
"""

comment_name_uz = """
🖋 Ismingizni kiriting
"""

comment_name_en = """
🖋 Enter your name
"""

comment_name_ru = """
🖋 Введите свое имя
"""

comment_attribution_uz = \
"""
<b>✅ Yuborgan izohingiz adminga jo'natilda, ajratgan vaqtingiz uchun raxmat.</b>
"""

comment_attribution_en = \
"""
<b>✅ Thank you for sending you the message from the admin that you deleted.</b>
"""

comment_attribution_ru = \
"""
<b>✅ Комментарий, который вы отправляете, отправляется администратору, спасибо за уделенное время.</b>
"""

comment_cancel_uz = \
"""
<b>🛑 Bekor qilish uchun ariza mavjud emas!</b>
"""


comment_cancel_en =\
"""
<b>🛑 There is no application for cancellation!</b>
"""

comment_cancel_ru = \
"""
<b>🛑 Заявки на отмену работы нет!</b>
"""


comment_cancel_current_uz =\
"""
<b>🛑Joriy fikr bekor qilindi</b>
"""


comment_cancel_current_en = \
"""
<b>🛑 The current opinion has been reversed/b>
"""

comment_cancel_current_ru = \
"""
<b>🛑текущая идея отменена</b>
"""

comment_error_uz = \
"""
<b>🤝 Iltimos pastdagi tugmalardan birini tanlang</b>
"""

comment_error_en = \
"""
<b>🤝 Please select one of the buttons at the bottom</b>
"""

comment_error_ru = \
"""
<b>🤝 Пожалуйста, выберите одну из кнопок ниже</b>
"""


SUCCES_TAKE_UZ = """
<b>
✅ Buyurtmangiz tasdiqlandi

admin javobini kuting

</b>
"""

SUCCES_TAKE_EN = """
<b>
✅ Order confirmed

wait for admin response

</b>
"""

SUCCES_TAKE_RU = """
<b>
✅ Подтвержденный заказ

дождитесь ответа администратора

</b>
"""

SUCCES_TAKE = {
    'uz': SUCCES_TAKE_UZ,
    'en': SUCCES_TAKE_EN,
    'ru': SUCCES_TAKE_RU,
}




PREPARING_UZ = \
"""
Hurmatli mijoz buyurtmangiz tayyorlanmoqda 🧑‍🍳
"""

PREPARING_EN = \
"""
Dear Customer your order is preparing 🧑‍🍳
"""

PREPARING_RU = \
"""
Уважаемый клиент ваш заказ готовится 🧑‍🍳
"""

PREPARING_TAKE = {
    'uz': PREPARING_UZ,
    'en': PREPARING_EN,
    'ru': PREPARING_RU,
}


READY_UZ = \
"""
<b>
Buyurtmangiz tayyor hurmatli mijoz
yoqimli ishtaha 🙂
</b>
"""

READY_EN = \
"""
<b>
Your order is ready Dear customer
pleasant appetite 🙂
</b>
"""

READY_RU = \
"""
<b>
Ваш заказ готов Уважаемый клиент
приятного аппетита 🙂
</b>
"""


SUCCESS = \
"""
✅ Buyurtma Tasdiqlandi
"""




READY_TAKE = {
    'uz': READY_UZ,
    'en': READY_EN,
    'ru': READY_RU,
}


DELIVERY_STATUS_ERROR = \
"""
Hurmatli mijoz Yetkazib berish vaqtida Yuzaga kelgan xatolar uchun uzur so'raymiz
"""



THAKS_SERVICES_UZ = """
<b>
West botdan foydalanganingiz uchun rahmat
Yoqimli ishtaha 😋
</b>
"""

THAKS_SERVICES_EN = """
<b>
Thank you for using West bot
Pleasant appetite 😋
</b>
"""

THAKS_SERVICES_RU = """
<b>
Спасибо за использование West bot
Приятного аппетита 😋
</b>
"""

THAKS_SERVICES_DELIVERY = {
    'uz': THAKS_SERVICES_UZ,
    'en': THAKS_SERVICES_EN,
    'ru': THAKS_SERVICES_RU,
}

DAMAGET_ERROR_UZ = \
"""
Hurmatli mijoz Yetkazib berish vaqtidagi xato va kamchiliklardan uzur so'raymiz
"""

DAMAGET_ERROR_EN = \
"""
Dear customer, we ask for forgiveness from errors and shortcomings in delivery time
"""

DAMAGET_ERROR_RU = \
"""
Уважаемый клиент приносим извинения за ошибки и упущения при доставке
"""


DAMAGET_ERROR = {
    'uz': DAMAGET_ERROR_UZ,
    'en': DAMAGET_ERROR_EN,
    'ru': DAMAGET_ERROR_RU,
}


THAKS_SERVICES = {
    'uz': "Botdan foydalanganigiz uchun rahmat",
    'en': "Thank you for using the bot",
    'ru': "Спасибо за использование бота",
}


THAKS_SERVICES_COMMENT = {
    'uz': "Botdan haqida fikr bildirganingiz uchun rahmat",
    'en': "Thank you for commenting on Botdan",
    'ru': "Спасибо за комментарий от бота",
}


UNKNOWN_ERROR_UZ = \
"""
Kechirasiz Hurmatli mijoz Noma'lum xatolik yuz berdi!\nBir ozdan keyin uzinib ko'ring!
"""

UNKNOWN_ERROR_EN = \
"""
Sorry, I couldn't do it!and then also with pleasure!
"""

UNKNOWN_ERROR_RU = \
"""
Извините, Уважаемый клиент, произошла неизвестная ошибка!\п попробуйте отключиться через некоторое время!
"""

UNKNOWN_ERROR = {
    "uz":UNKNOWN_ERROR_UZ,
    "en":UNKNOWN_ERROR_EN,
    "ru":UNKNOWN_ERROR_RU
}


PREPARING_FOOD_UZ = """
Sizning buyurtmangiz tayyorlanmoqda ⌛
"""

PREPARING_FOOD_RU = """
Ваш заказ готовится ⌛
"""

PREPARING_FOOD_EN = """
Your order is preparing ⌛
"""

PREPARING_FOOD = {
    'uz': PREPARING_FOOD_UZ,
    'ru': PREPARING_FOOD_RU,
    'en': PREPARING_FOOD_EN,
}

PREPARING = """
<b>
Tayyorlanmoqda

{}
</b>
"""





DELIVER_SPEED = """
<b>
🏃‍♂️ km bo'yicha narxni belgilang

</b>
"""

THERE_ACCEPT_DELIVERY_UZ = """
<b>
✅ Buyurtmalaringiz yuborildi

Buyurtmangiz tez orada yetib boradi
Yetkazib berish narxi: bepul.

</b>
"""

THERE_ACCEPT_DELIVERY_EN = """
<b>
✅ Your orders sent

Your order will arrive soon
Delivery price: free.
</b>
"""

THERE_ACCEPT_DELIVERY_RU = """
<b>
✅ Ваши заказы отправлены

Ваш заказ скоро прибудет.
Стоимость доставки: бесплатно.
</b>
"""

THERE_ACCEPT_DELIVERY = {
    'uz': THERE_ACCEPT_DELIVERY_UZ,
    'en': THERE_ACCEPT_DELIVERY_EN,
    'ru': THERE_ACCEPT_DELIVERY_RU,
}





FIVE_ACCEPT_DELIVERY_UZ = """
<b>
✅ Buyurtmalaringiz yuborildi

Buyurtmangiz tez orada yetib boradi.
Yetkazib berish narxi: 15 ming so'm.

</b>
"""

FIVE_ACCEPT_DELIVERY_EN = """
<b>
✅ Your orders sent

Your order will arrive soon
Delivery price: Rs 15,000.
</b>
"""

FIVE_ACCEPT_DELIVERY_RU = """
<b>
✅ Ваши заказы отправлены

Ваш заказ скоро прибудет
Стоимость доставки: 15 тысяч сумов.
</b>
"""


FIVE_ACCEPT_DELIVERY = {
    'uz': FIVE_ACCEPT_DELIVERY_UZ,
    'en': FIVE_ACCEPT_DELIVERY_EN,
    'ru': FIVE_ACCEPT_DELIVERY_RU,
}



EIGHT_ACCEPT_DELIVERY_UZ = """
<b>
✅ Buyurtmalaringiz yuborildi

Buyurtmangiz tez orada yetib boradi
Yetkazib berish narxi: 25 ming so'm.

</b>
"""

EIGHT_ACCEPT_DELIVERY_EN = """
<b>
✅ Your orders sent

Your order will arrive soon
Delivery price: Rs 15,000.
</b>
"""

EIGHT_ACCEPT_DELIVERY_RU = """
<b>
✅ Ваши заказы отправлены

Ваш заказ скоро прибудет
Стоимость доставки: 25 тысяч сумов.
</b>
"""



EIGHT_ACCEPT_DELIVERY = {
    'uz': EIGHT_ACCEPT_DELIVERY_UZ,
    'en': EIGHT_ACCEPT_DELIVERY_EN,
    'ru': EIGHT_ACCEPT_DELIVERY_RU,
}



TEN_ACCEPT_DELIVERY_UZ = """
<b>
✅ Buyurtmalaringiz yuborildi

Buyurtmangiz tez orada yetib boradi.
Yetkazib berish narxi: 30 ming so'm.

</b>
"""

TEN_ACCEPT_DELIVERY_EN = """
<b>
✅ Your orders sent

Your order will arrive soon.
Delivery price: Rs 30,000.
</b>
"""

TEN_ACCEPT_DELIVERY_RU = """
<b>
✅ Ваши заказы отправлены

Ваш заказ скоро прибудет.
Стоимость доставки: 30 тысяч сумов.
</b>
"""

TEN_ACCEPT_DELIVERY = {
    'uz': TEN_ACCEPT_DELIVERY_UZ,
    'en': TEN_ACCEPT_DELIVERY_EN,
    'ru': TEN_ACCEPT_DELIVERY_RU,
}



HIGH_ACCEPT_DELIVERY_UZ = \
"""
<b>
West Restoranidan sizning manzilingiz o'rtasidagi masofa [ 10 km ]dan yuqori
bo'lganligi sababli Kuryer siz bilan bog'lanadi.

kuryer qo'ng'irog'ini kuting
</b>
"""

HIGH_ACCEPT_DELIVERY_EN = \
"""
<b>
The distance between your destination from the West restaurant is more than [ 10 km ]
since there is a courier will contact you.
wait for The Courier call
</b>
"""

HIGH_ACCEPT_DELIVERY_RU = \
"""
<b>
Расстояние от ресторана West до места назначения более [ 10 км ].
потому что курьер свяжется с вами.
ждите курьерского звонка
</b>
"""

HIGH_ACCEPT_DELIVERY = {
    'uz': HIGH_ACCEPT_DELIVERY_UZ,
    'en': HIGH_ACCEPT_DELIVERY_EN,
    'ru': HIGH_ACCEPT_DELIVERY_RU,
}




ORDER_SUCCES_SEND_UZ = """
<b>
✅ Buyurtma qabul qilindi

Buyurtma qanday holatda yetib bordi ?
</b>
"""

ORDER_SUCCES_SEND_ADMIN_UZ = """
<b>
✅ Sizning buyurtmangiz yuborildi
adminlarimiz tez orada javob berishadi
</b>
"""

ORDER_SUCCES_SEND_ADMIN_EN = """
<b>
✅ Your order sent
our admins will respond soon
</b>
"""

ORDER_SUCCES_SEND_ADMIN_RU = """
<b>
✅ Ваш заказ отправлен
наши админы скоро ответят
</b>
"""

ORDER_SUCCES_SEND_ADMIN = {
    "uz":ORDER_SUCCES_SEND_ADMIN_UZ,
    "en":ORDER_SUCCES_SEND_ADMIN_EN,
    "ru":ORDER_SUCCES_SEND_ADMIN_RU
}

DELIVERY_DECLINE = "⚠️ Buyurtma nima sababdan bekor qilindi?"

NEW_DELIVER_ERROR_EMPTY_FOOD_UZ = """
<b>
Siz buyurtma qilgan maxsulotlar qolmaganligi sababli hozirda  buyurtmani yetkazib berolmaymiz 😔
Uzur so'raymiz xurmatli mijoz ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_FOOD_EN = """
<b>
We can't deliver your order now because there are no products left to order 😔
Long ask Dear customer ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_FOOD_RU = """
<b>
Мы не можем доставить заказ прямо сейчас, потому что у вас не осталось заказанных вами продуктов 😔
Извините, Уважаемый клиент ❗ ️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_FOOD = {
    "uz":NEW_DELIVER_ERROR_EMPTY_FOOD_UZ,
    "cr":NEW_DELIVER_ERROR_EMPTY_FOOD_EN,
    "ru":NEW_DELIVER_ERROR_EMPTY_FOOD_RU
}



NEW_DELIVER_ERROR_EMPTY_KURIER_UZ = """
<b>
Ayni vaqta bo'sh kuryerlarimiz bo'lmaganligi sababli buyurtmani yetkazib berolmymiz. 😔
iltimos birozdan so'ng urinib ko'ring ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_KURIER_EN = """
<b>
We can deliver the order because we do not have empty couriers at the moment. 😔
please try a little later ❗️
</b>
"""

NEW_DELIVER_ERROR_EMPTY_KURIER_RU = """
<b>
Поскольку на данный момент у нас нет свободных курьеров, мы не можем доставить заказ. 😔
пожалуйста, попробуйте немного позже ❗ ️
</b>
"""

NEW_DELIVER_ERROR_OTHER_UZ = """
<b>
Noma'lum xatolik yuz berganligi sababli buyurtmani yetkazib berolmymiz. 😔
iltimos birozdan so'ng urinib ko'ring ❗️
</b>
"""

NEW_DELIVER_ERROR_OTHER_EN = """
<b>
We cannot buy because of an unknown error. 😔
please try it a little later and check it out.
</b>
"""

NEW_DELIVER_ERROR_OTHER_RU = """
<b>
Мы не можем доставить заказ из-за неизвестной ошибки. 😔
пожалуйста, сообщите об этом чуть позже ❗️
</b>
"""


ANSWER_IS_GIVEN_UZ = \
"""
Buyurtmangiz bekor qilindi.
Chunki siz admin qo'ng'irog'iga javob bermadingiz.
"""

ANSWER_IS_GIVEN_RU = \
"""
Ваш заказ отменен.
Потому что вы не ответили на вызов администратора.
"""

ANSWER_IS_GIVEN_EN = \
"""
Your order cancelled.
Because you didn't answer an admin call.
"""




ORDER_OTMEN_UZ = \
"""
Buyurtmangiz bekor qilindi.
Chunki siz bekor qildingiz.
"""

ORDER_OTMEN_RU = \
"""
Ваш заказ отменен.
Потому что ты отменил.
"""

ORDER_OTMEN_EN = \
"""
Your order has been canceled.
Because you canceled.
"""





NEW_DELIVER_ERROR = {
    'empty_food':{
        'uz':NEW_DELIVER_ERROR_EMPTY_FOOD_UZ,
        'en':NEW_DELIVER_ERROR_EMPTY_FOOD_EN,
        'ru':NEW_DELIVER_ERROR_EMPTY_FOOD_RU,
    },
    'empty_kurier':{
        'uz':NEW_DELIVER_ERROR_EMPTY_KURIER_UZ,
        'en':NEW_DELIVER_ERROR_EMPTY_KURIER_EN,
        'ru':NEW_DELIVER_ERROR_EMPTY_KURIER_RU,
    },
    'other':{
        'uz':NEW_DELIVER_ERROR_OTHER_UZ,
        'en':NEW_DELIVER_ERROR_OTHER_EN,
        'ru':NEW_DELIVER_ERROR_OTHER_RU,
    },
    'answer_is_given':{
        'uz':ANSWER_IS_GIVEN_UZ,
        'en':ANSWER_IS_GIVEN_EN,
        'ru':ANSWER_IS_GIVEN_RU,
    },
    'order_otmen':{
        'uz':ORDER_OTMEN_UZ,
        'en':ORDER_OTMEN_EN,
        'ru':ORDER_OTMEN_RU,
    },

}




def format_price(price):
    return f"{price:,}".replace(',', ' ')

def H_DELIVERY(**kwargs):
    new_order_message_text = ""
    total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi
    new_order_message_text += f"\n\n"

    new_order_message_text += f"Buyurtma turi: 🚖 Yetkazib berish\n"
    new_order_message_text += f"Ism: {kwargs['fullname']}\n"
    new_order_message_text += f"Telefon: <a href='{kwargs['phone']}\n'>{kwargs['phone']}</a>\n"
    # new_order_message_text += f"To'lov usuli: {kwargs['payment']}\n"
    new_order_message_text += f"Izohlar: {kwargs['add_note']}\n"
    new_order_message_text += f"To'lov turi: {kwargs['payment_type']}\n"
    new_order_message_text += f"Manzil: {kwargs['location_name']}\n\n"

    for i in kwargs['basket']:
        item_name = i['food']['name_uz']
        item_count = i['count']
        item_price = i['food']['price']
        item_total = item_count * item_price

        formatted_item_price = format_price(item_price)
        formatted_item_total = format_price(item_total)

        new_order_message_text += f"\n{item_name}\n"
        new_order_message_text += f"{item_count} X {formatted_item_price} so'm = {formatted_item_total} so'm\n"

        total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

    formatted_total_price = format_price(total_price)
    # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
    new_order_message_text += f"\nUmumiy narx: {formatted_total_price} so'm\n"

    return new_order_message_text









def format_price(price):
    return f"{price:,}".replace(',', ' ')

def NEW_DELIVERY(**kwargs):
    new_order_message_text = ""
    total_price = 0  # Umumiy narxni hisoblash uchun o'zgaruvchi
    new_order_message_text += f"\n\n"

    new_order_message_text += f"Buyurtma turi: 🚖 Yetkazib berish\n"
    new_order_message_text += f"Ism: {kwargs['fullname']}\n"
    new_order_message_text += f"Telefon: <a href='{kwargs['phone']}\n'>{kwargs['phone']}</a>\n"
    # new_order_message_text += f"To'lov usuli: {kwargs['payment']}\n"
    new_order_message_text += f"Izohlar: {kwargs['add_note']}\n"
    new_order_message_text += f"To'lov turi: {kwargs['payment_type']}\n"
    new_order_message_text += f"Manzil: {kwargs['location_name']}\n\n"

    for i in kwargs['basket']:
        item_name = i['food']['name_uz']
        item_count = i['count']
        item_price = i['food']['price']
        item_total = item_count * item_price

        formatted_item_price = format_price(item_price)
        formatted_item_total = format_price(item_total)

        new_order_message_text += f"\n{item_name}\n"
        new_order_message_text += f"{item_count} X {formatted_item_price} so'm = {formatted_item_total} so'm\n"

        total_price += item_total  # Har bir mahsulot narxini umumiy narxga qo'shish

    formatted_total_price = format_price(total_price)
    # Umumiy narxni savatdagi mahsulotlar ro'yxati oxirida qo'shish
    new_order_message_text += f"\nUmumiy narx: {formatted_total_price} so'm\n"

    return new_order_message_text




def NEW_COMMENT(**kwargs):
    new_order_message_text = ""
    total_price = 0

    new_order_message_text += f"\n\n"
    new_order_message_text += f"Baholash:  <a href='{kwargs['comment']}\n'>{kwargs['comment']}</a>\n"

    return new_order_message_text


def NEW_TAKE(**kwargs):
    new_order_message_text = ""
    total_price = 0

    for i in kwargs['basket']:
        price = i['count'] * i['food']['price']
        total_price += price

        new_order_message_text += f"{i['food']['name_uz']}:  {i['count']} X {i['food']['price']} 000 so'm = {price}\n 000 so'm"

    new_order_message_text += f"\n\n"
    new_order_message_text += f"💵 {total_price} 000 so'm\n"
    new_order_message_text += f"📞 {kwargs['phone']}\n"
    new_order_message_text += f"⌚️ Olib Ketish vaqti: {kwargs['time']}"

    return new_order_message_text


EMPTY_BASKET_UZ = """
<b>
Sizning savatingiz bo'sh, buyurtma berish uchun mahsulot tanlang
</b>
"""

EMPTY_BASKET_RU = """
<b>
Ваша корзина пуста, выберите товар для заказа
</b>
"""

EMPTY_BASKET_EN = """
<b>
Your basket is empty, choose a product to order
</b>
"""

EMPTY_BASKET = {
    "uz":EMPTY_BASKET_UZ,
    "ru":EMPTY_BASKET_RU,
    "en":EMPTY_BASKET_EN,
}




comment_uz = """
Fikringizni kiriting
"""

comment_en = """
Enter your opinion
"""

comment_ru = """
Введите свое мнение
"""

# Setting tugmasining bo'shlanish'

settings_text_uz = """
<b>Ma'lumotlarni o'zgartirish uchun quyidagi tugmalardan foydalanishingiz mumkin.</b>
"""

settings_text_en = """
<b>You can use the following buttons to change the data.</b>
"""

settings_text_ru = """
<b>Вы можете использовать следующие кнопки для изменения данных.</b>
"""

SETTINGS_TEXT = {
    'uz': settings_text_uz,
    'ru': settings_text_ru,
    'en': settings_text_en,
}

# Setting tugmasining tugallanish'

# ortga qaytish tugmasini bo'shlanishi'

back_uz = """
Asosiy menyuga qaytdingiz
"""

back_en = """
Back to the main menu
"""

back_ru = """
Вы вернулись в Главное меню
"""

# ortga qaytish tugmasini tuggalanish'


# userlani ro'yhatdan o'tkazish bo'shlanishi'


PHONE_UZ = \
"""
📱 Raqamni +998 ** *** ** ** shakilda yuboring.
"""

PHONE_EN = \
"""
Send  your phone number .

Send  phone number  for calls in the format:
 + 998 ** *** ****
"""

PHONE_RU = \
"""
Отправьте ваш номер телефона.

Отправьте номер телефона для звонков в формате:
+998 ** *** ****
"""

PHONE = {
    "uz": PHONE_UZ,
    "en": PHONE_EN,
    "ru": PHONE_RU,
}

update_lang = \
"""
Til o'zgartirildi
"""


TAKE_PHONE_UZ = \
"""
Iltimos telefon raqamingizni kiriting.
yoki "📞 Raqamni jo'natish" yuborish tugmasini bosing
"""
# 📞 Raqamni jo'natish
TAKE_PHONE_RU = \
"""
Пожалуйста, введите свой номер телефона.
или нажмите кнопку" отправить📞 номер"
"""

TAKE_PHONE_EN = \
"""
📞 Please enter your phone number.
or click send "send number"
"""
# 📞 Отправить номер

PHONE_DELIVERY = {
    'uz': TAKE_PHONE_UZ,
    'ru': TAKE_PHONE_RU,
    'en': TAKE_PHONE_EN
}


SUCCES_BASKET = {
    'uz':"<b>✅ Sizning maxsulotlaringiz savatga qo'shildi</b>",
    'en':"<b>✅ Your products have been added to the basket</b>",
    'ru':"<b>✅ ваши товары добавлены в корзину</b>",
}

PHONE_ERROR_UZ =\
"""
<b>
❗️ Iltimos telefon raqamingizni to'g'ri kiriting

<code>1. Faqat raqamlardan foydalanish kerak</code>
<code>2. Uzunligi 9 ta raqamdan iborat bo'lishi kerak</code>
<code>3. Bo'sh joylar bo'lmasin</code>
</b>
"""

PHONE_ERROR_EN =\
"""
<b>
❗️ Илтимос telefon рақамингизни тўғри киритинг

<cоде>1. Only numbers must be used</cоде>
<cоде>2. The length should consist of 9 digits</cоде>
<cоде>3. Let there be no vacancies</cоде></b>
</.b>
"""
PHONE_ERROR_RU =\
"""
<b>
❗ ️ Пожалуйста, введите свой номер телефона правильно

<code>1. Нужно использовать только цифры< / code>
<code>2. Длина должна быть 9 цифр< / code>
<code>3. Нет пробелов< / code>
</b>
"""

PHONE_ERROR = {
    'uz':PHONE_ERROR_UZ,
    'cr':PHONE_ERROR_EN,
    'ru':PHONE_ERROR_RU,
}

# userlani ro'yhatdan o'tkazish tugallanishi'

# Asosiy menyuni bo'shlanishi'

MAIN_MENU_UZ = \
"""
<b>
Xayrli kun {}.

West botga xush kelibsiz !
</b>
"""

MAIN_MENU_EN = """
Good day{}

Welcome to West bot !
"""

MAIN_MENU_RU = """
Добрый день {}

Добро пожаловать в West bot !
"""

MAIN_MENU = {
    'uz':MAIN_MENU_UZ,
    'en':MAIN_MENU_EN,
    'ru':MAIN_MENU_RU,
}


CATEGORY_NOT_FOUND = {
    'uz': "Kechirasiz, {} kategoriyasidagi ovqatlar topilmadi.",
    'ru': "Извините, блюда в категории {} не найдены.",
    'en': "Sorry, no foods found in the {} category."
}

lang_switch_handler_uz = \
"""
✅ Til muffaqiyatli almashtirildi

📝 Asosiy menyuga qaytingiz
"""

lang_switch_handler_en = \
"""
✅ Language muffled replaced

📝 Return to main menu
"""

lang_switch_handler_ru = \
"""
✅ Язык успешно заменен

📝 Вернуться в Главное меню
"""


phone_switch_handler_uz = \
"""
✅ Telifon raqam muffaqiyatli almashtirildi

📝 Asosiy menyuga qaytingiz
"""

phone_switch_handler_en = \
"""
✅ Telifon number muffled replaced

📝 Return to main menu
"""

phone_switch_handler_ru = \
"""
✅ Телефон номер успешно заменен

📝 Вернуться в Главное меню
"""


# Asosiy menyuni tugallanishi'

# Categoryalarni bo'shlanishi'

CATEGORY_UZ = \
"""
<b>
Iltimos kategoriyani tanlang
</b>
"""

CATEGORY_EN = \
"""
<b>
Please Select Category
</b>
"""
CATEGORY_RU = \
"""
<b>
Пожалуйста, выберите категорию
</b>
"""

CATEGORY = {
    'uz':CATEGORY_UZ,
    'en':CATEGORY_EN,
    'ru':CATEGORY_RU
}

FOODS = {
    "uz": "<b>Toifani va miqdorni tanlang </b>",
    "en": "<b>Choose a category and a mixer </b>",
    "ru": "<b>Выберите еду и количество </b>",
}




COUNT = \
"""
<b>{}</b>
<b>{} X {} = {} 000 so'm</b>

<b>{}</b> 000 so'm

<b>{}</b>

"""

phone_switch_uz = \
"""
📞 Telifon Raqamni o'zgartirish uchun pastadagi tugmani bosing yoki yangi raqam kiriting
"""

phone_switch_en = \
"""
📞 Telifon press the button on the paste or enter a new number to change the number
"""

phone_switch_ru = \
"""
📞 Телефон нажмите кнопку в петле или введите новый номер, чтобы изменить номер
"""


# endswitch



# tilni almashtirish tugmasini bo'shlanishi'

lang_switch_uz = """
Tilni almashtirish
"""

lang_switch_en = """
Language switching
"""

lang_switch_ru = """
Переключение языка
"""

# tilni almashtirish tugmasini tugallanishi'

location_uz = """
Manzilni kiriting
"""

location_en = """
Enter address
"""

location_ru = """
Введите адрес
"""

order_delivery_uz = """
Sizning buyurtmangiz Adminga jo'natildi
"""

order_delivery_en = """
Your order was sent to Admin
"""

order_delivery_ru = """
Ваш заказ был отправлен администратору
"""

take_time_uz = """
<b>
Olib ketish vaqtini kiriting.
Misol uchun ➡️ <i>12:00</i>
</b>
"""

take_time_en = """
Enter the take-away time.
For example ➡️ <i>12: 00</i>
"""

take_time_ru = """
<b>
Введите время получения.
Напримерol ➡️ <i>12:00</i>
</b>
"""

phone_rule_uz = """
📝 Iltimos raqamda kiriting
"""
phone_rule_en = """
📝 Please enter in the number
"""
phone_rule_ru = """
📝 Введите номер
"""


time_rule_uz = """
📝 Iltimos raqamda kiriting
"""
time_rule_en = """
📝 Please enter in the number
"""
time_rule_ru = """
📝 Введите номер
"""

time_e = {
    'uz': time_rule_uz,
    'ru': time_rule_ru,
    'en': time_rule_en,
}


phone_nomer_len_rule_uz = """
📞Telifon raqam eng kamida 9 ta sondan iborat bo'lish kerak❌
"""

phone_nomer_len_rule_en = """
📞 Telifon number must consist of at least 9 numbers ❌
"""

phone_nomer_len_rule_ru = """
📞Телефон номер должен состоять как минимум из 9 цифр❌
"""

PHONE_SWITCH_E = {
    'uz': phone_nomer_len_rule_uz,
    'ru': phone_nomer_len_rule_ru,
    'en': phone_nomer_len_rule_en,
}


your_basket_uz = \
"""
<b>🛒 Sizning maxsulotlaringiz</b> \n
"""


your_basket_en = \
"""
<b>🛒 Your products</b> \n
"""

your_basket_ru = \
"""
<b>🛒 Ваши продукты</b> \n
"""


information_uz = \
"""
Milliondan ortiq mijozlar tashrif buyurgan!

West Restorani haqida qisqacha,west restorani 2010 yildan o'z foalyatini boshlagan bo'lib, shu vaqt ichida milliondan ortiq tashrif buyuruvchilarga xizmat ko'rsatishga muvaffaq bo'ldik va nafaqat poytaxt aholisi, balki uning mehmonlari uchun ham diqqatga sazovor markazga aylandik!
West restoraning Manzili  Toshkent, Mirobod ko'chasi 1-etaj joylashgan.


🕰 Ish soatlari

Dushanba: 11:00 – 01:00
Seshanba: 11:00 – 01:00
Chorshanba: 11:00 – 01:00
Payshanba: 11:00 – 01:00
Juma: 11:00 – 01:00
Shanba: 11:00 – 01:00
Yakshanba: 11:00 – 01:00



📝 O'ziga xos jihatlari!

🚗 Taomni tez va sifatli yetkazib berish
🚶‍♂️ Olib ketishingiz uchun o'z vaqtida  tayyorlab qo'yish
✅ Hamyonbop va sifatli taomlar!

Aniqroq ma'lumot va Manzilni ko'rish uchun pastdagi Malumotlarni ko'rish tugmasini bosing!

📞 Biz bilan bog'lanish uchun +998938870000
"""


information_en = \
"""
More than a million customers have visited!

Briefly about the West restaurant, The West restaurant began its foality from 2010, during which time we managed to serve more than a million visitors and become a center of attraction not only for residents of the capital, but also for its guests!
The address of the West restaurant is Tashkent, mirabad Street 1-etaj.


🕰 Working hours

Monday: 11:00 – 01:00
Tuesday: 11:00 – 01:00
Wednesday: 11:00 – 01:00
Thursday: 11:00 – 01:00
Friday: 11:00 – 01:00
Saturday: 11:00 – 01:00
Sunday: 11:00 – 01:00



📝 Specific aspects!

🚗 Fast and high-quality food delivery
🚶 ♂ ️ Ready in time for you to take
✅ Affordable and quality dishes!

Click the view information button below to see more specific information and address!

📞 To contact us +998938870000
"""

information_ru = \
"""
Посетили более миллиона клиентов!

Вкратце о ресторане West,ресторан West начал свою деятельность с 2010 года, за это время мы успели обслужить более миллиона посетителей и стать изюминкой не только для жителей столицы, но и для ее гостей!
Адрес ресторана West: Ташкент, улица Мирабад, 1 этаж.


♦ Часы работы

Понедельник: 11:00 – 01: 00
Вторник: 11: 00 – 01:00
Среда: 11:00 – 01:00
Четверг: 11:00 – 01:00
Пятница: 11:00 – 01: 00
Суббота: 11:00 – 01: 00
Воскресенье: 11:00 – 01:00



Особенности работы!

♦ Быстрая и качественная доставка еды
🚶♂️ Своевременно подготовить для вас еду на вынос
♦ Доступная и качественная еда!

Нажмите кнопку "просмотреть информацию" ниже, чтобы увидеть более точную информацию и местоположение!

📞 +998938870000, чтобы связаться с нами
"""



location_info_uz = \
"""
https://yandex.uz/maps/10335/tashkent/house/YkAYdAFoT0QCQFprfX54dnpgZA==/?ll=69.268648%2C41.297337&z=19.22
"""



error_count_uz = \
"""
❌ Kechirasiz mahsulot sonini xato kiritingiz  qaytadan urinib ko'ring
"""



contact_uz = \
"""
Biz bilan bog'lanish uchun:
📞 +998 93-887-00-00
"""

contact_en = \
"""
To contact us:
📞 +998 93-887-00-00
"""

contact_ru = \
"""
Чтобы связаться с нами:
📞 +998 93-887-00-00
"""



REMOVE_BUTTON_UZ = \
"""
To'lovni amalga oshirganingizdan so'ng buyurtmangiz adminga yuboriladi.
"""

REMOVE_BUTTON_RU = \
"""
После оплаты ваш заказ будет отправлен администратору.
"""

REMOVE_BUTTON_EN = \
"""
After making the payment, your order will be sent to the admin.
"""

REMOVE_BUTTON = {
    'uz': REMOVE_BUTTON_UZ,
    'ru': REMOVE_BUTTON_RU,
    'en': REMOVE_BUTTON_EN,
}