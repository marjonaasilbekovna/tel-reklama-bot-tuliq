from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

add = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Reklama qo'shish ➕"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt yuborish ☎️", request_contact=True)]
    ],
    resize_keyboard=True,
)