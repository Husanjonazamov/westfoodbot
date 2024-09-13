from datetime import datetime, time
import pytz


# Ishlash vaqtlarini yangilang
MORNING_START = time(11, 30)  # 11:30
NIGHT_END = time(23, 30)      # 23:30



def is_within_working_hours() -> bool:
    """Tekshirish funksiyasi"""
    timezone = pytz.timezone('Asia/Tashkent')
    now = datetime.now(timezone).time()
    return MORNING_START <= now <= NIGHT_END

