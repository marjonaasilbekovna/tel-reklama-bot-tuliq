from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.admin_keyboard import add

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) 
        await message.answer(text=f"Assalomu alaykum {full_name}\n Hurmatli foydalanuvchi.\nTelefonlar uchun reklama botimizga hush kelibsiz. Bu bot sizga telefoningizni ishonchli sota olishingizni ta'minlaydi. \n\nSiz telefon uchun reklama bermoqchi bo'lsangiz 'Reklama qo'shish +' tugmasini bosing 👇🏻", reply_markup=add)
    except:
        await message.answer(text=f"Assalomu alaykum {full_name} \nHurmatli foydalanuvchi.\nTelefonlar uchun reklama botimizga hush kelibsiz. Bu bot sizga telefoningizni ishonchli sota olishingizni ta'minlaydi. \n\nSiz telefon uchun reklama bermoqchi bo'lsangiz 'Reklama qo'shish +' tugmasini bosing 👇🏻", reply_markup=add)
