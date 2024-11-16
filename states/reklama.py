from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

class Reklama(StatesGroup):
    rasm  = State()
    nomi = State()
    xotira = State()
    dakument = State()
    holati = State()
    yili = State()
    rang = State()
    tel = State() 
    tg_user = State()
    shahar = State()
