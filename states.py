from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    lang = State()
    phone = State()
    fullname = State()

class FoodOrder(StatesGroup):
    order = State()
    location = State()
    location_check = State()
    category = State()
    food = State()
    count = State()

class UpdateRegister(StatesGroup):
    lang = State()
    phone = State()

class Comments(StatesGroup):
    commen_ball = State()
    comment = State()
    register_commit = State()

class Delivery(StatesGroup):
    addComment = State()
    location = State()
    location_check = State()
    phone = State()
    payment = State()
    attribution_send = State()
    preparing = State()
    click = State()




class TakeAway(StatesGroup):
    phone = State()
    time = State()



class Basket(StatesGroup):
    clear = State()



class UpdateRegisterLang(StatesGroup):
    lang = State()

class UpdateRegisterPhone(StatesGroup):
    phone = State()

class UpdateRegisterFullname(StatesGroup):
    fullname = State()