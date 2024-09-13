import os
import logging
from bot.models import Basket, User
from pyclick import PyClick
from pyclick.views import PyClickMerchantAPIView
import requests
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
from django.utils.translation import gettext as _
from unittest.mock import Mock
from loader import API_TOKEN
from utils import buttons
from datetime import datetime


logger = logging.getLogger(__name__)


class OrderCheckAndPayment(PyClick):
    def check_order(self, order_id: str, amount: str):
        order = Basket.objects.filter(user__user_id=order_id)
        if not order:
            return self.ORDER_NOT_FOUND

        total_price = 0
        for i in order:
            total_price += i.food.price * i.count

        if total_price == int(amount):
            return self.ORDER_FOUND
        else:
            return self.INVALID_AMOUNT



    def successfully_payment(self, order_id: str, transaction: object):
        """ Called after a successful payment """
        logger.info(f"Order ID: {order_id}, Transaction: {transaction}")

        user_chat_id = order_id
        admin_chat_id = '-4233652666'

        # Get user information from User model
        try:
            
            user = User.objects.get(user_id=order_id)
            phone = user.phone
            lang = user.lang
        except User.DoesNotExist:
            phone = _("Unknown")
            lang = 'uz'

        amount = getattr(transaction, 'amount', None)
        timestamp = transaction.get('timestamp', None) if isinstance(transaction, dict) else None
        if not timestamp:
            timestamp = transaction.details.timestamp if hasattr(transaction, 'details') and hasattr(transaction.details, 'timestamp') else None
        check_id = getattr(transaction, 'check_id', None)

        # Format timestamp
        if timestamp:
            try:
                timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S %d.%m.%Y')
            except ValueError as e:
                # logger.error(f"Error parsing timestamp: {e}")
                timestamp = _("Invalid time format")
        else:
            timestamp = _("Unknown time")

        if lang == 'uz':
            message_to_user = "To'lov muvaffaqiyatli bajarildi! Buyurtmangizni adminga yuborish uchun pastdagi tugmani bosing"
            success_button = buttons.SUCCESS_FULY_APMENT_UZ
        elif lang == 'ru':
            message_to_user = "Оплата прошла успешно! Нажмите кнопку ниже, чтобы отправить свой заказ администратору"
            success_button = buttons.SUCCESS_FULY_APMENT_RU
        else:  # Default language is Uzbek
            message_to_user = "The payment was completed successfully! Click the button below to send your order to admin"
            success_button = buttons.SUCCESS_FULY_APMENT_EN

        # Send message to the user
        
        BOT_TOKEN = API_TOKEN
        
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": user_chat_id,
                "text": message_to_user,
                "reply_markup": json.dumps(success_button.to_python())  # Convert the button to JSON format
            }
        )

class OrderTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
