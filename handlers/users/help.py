from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🔥 Buyruqlar... \n\nBotdan foydalanish uchun '/start' - tugmasini bosing va reklama qo'shish uchun 'Reklama qo'shish +' - tugmasini bosing va kerakli malumotlarni kiriting. \n '/about' - Bot haqida qisqacha malumot uchun.\n\'/xabar'- adminga murojatingizni yozib qoldirishingiz mumkin.\n")
