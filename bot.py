
import os
from aiogram import executor
from loader import dp, bot


import user

async def on_startup(dp):

    # Adminlarga xabar yuborish
    ADMIN = os.getenv('ADMIN_ID')
    await bot.send_message(ADMIN, "Bot ishga tushdi!")

# disable skip_update deploy version
executor.start_polling(dp, skip_updates=False, on_startup=on_startup)