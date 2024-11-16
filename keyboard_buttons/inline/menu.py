from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="True"), InlineKeyboardButton(text="Bekor qilish ❌", callback_data="False")]
    ]
)


ask = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data="yes"), InlineKeyboardButton(text="Yo'q", callback_data="no")]
    ]
)