from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu bot sizga siz sotmoqchi bulgan telefoningiz uchun reklama tayyorlashga yordam beradi. Va siz osongina telefoningiz uchun reklama yaratib uni telefon reklamalari bo'lgan guruhga uni joylash, oson sotish imkonini beradi.\nAgar yordam kerak bo'lsa '/help' - tugmasini tanlab o'zingizga kerakli bo'lgan yordamni olishingiz mumkin.\nBot admini bilan bog'lanish uchun '/xabar' - tugmasini tanlang va murojaatingizni yozib qoldiring adminimiz siz bilan albatta bog'lanadi.\nMrojaat uchun tel :\n📞 +(998) 95-454-48-28\nBot yaratuvchilari 'Sifatedu' o'quv markazi.\nBizni tanlaganingizdan hursandmiz.")

