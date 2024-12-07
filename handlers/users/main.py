from aiogram.types import Message, CallbackQuery
from loader import dp, bot, ADMINS,CHANNELS
from aiogram import F
from aiogram.fsm.context import FSMContext
from states.reklama import Reklama
from aiogram.types import ReplyKeyboardRemove
from keyboard_buttons.inline.menu import ask, menu, yana
from keyboard_buttons.default.admin_keyboard import send_contact

@dp.message(F.text=="Reklama qo'shish ➕")
async def reklama(message:Message,state:FSMContext):
    await message.answer("Reklama telefon uchun 🖼 rasm kiriting !", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.rasm)

@dp.callback_query(F.data == "yana")
async def yana_reklama(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await callbeck.message.answer("Yana reklama berish uchun reklama qilmoqchi bo'lgan telefoningizni rasmini kiriting:")
    await state.set_state(Reklama.rasm)

@dp.message(F.photo, Reklama.rasm)
async def reklama_rasm(message: Message, state: FSMContext):
    if message.photo:
        photo = message.photo[-1].file_id
        await state.update_data(photo=photo)
        await message.answer("Telefonni nomini kiriting!")
        await state.set_state(Reklama.nomi)

@dp.message(Reklama.rasm)
async def reklama_rasm_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon rasmini kiriting ❗️")

@dp.message(F.text, Reklama.nomi)
async def reklama_nomi(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Telefon xotira hajmini kiriting !")
    await state.set_state(Reklama.xotira)

@dp.message(Reklama.nomi)
async def reklama_nomi_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon nomini tug'ri kiriting ❗️")


@dp.message(F.text, Reklama.xotira)
async def reklama_xotira(message:Message,state:FSMContext):
    xotira = message.text
    await state.update_data(xotira=xotira)
    await message.answer("Karopka dakument bormi yoki yo'qmi", reply_markup=ask)
    await state.set_state(Reklama.dakument)

@dp.message(Reklama.xotira)
async def reklama_xotira_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon xotirasini tug'ri kiriting ❗️")


@dp.callback_query(F.data == "yes")
async def reklama_yes(callbeck:CallbackQuery,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Bor")
    await callbeck.message.answer("Telefonnig holati haqida yozing !")
    await state.set_state(Reklama.holati)


@dp.callback_query(F.data == "no")
async def reklama_no(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    await state.update_data(dakument="Yo'q")
    await callbeck.message.answer("Telefonnig holati haqida yozing !")
    await state.set_state(Reklama.holati)

@dp.message(Reklama.dakument)
async def reklama_dakument_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos dakumentning bor yoki yo'qligini tugmalardan tanlang ❗️")



#-----------------daument state ti inline bilan qilindi------------------------------
# @dp.message(Reklama.dakument)
# async def reklama(message:Message,state:FSMContext):
#     await state.update_data(=)
#     await message.answer("")
#     await state.set_state(Reklama.holati)  

@dp.message(F.text, Reklama.holati)
async def reklama_holat(message:Message,state:FSMContext):
    holat = message.text
    await state.update_data(holat=holat)
    await message.answer("Telefon ishlab chiqilgan yilini kiriting !")
    await state.set_state(Reklama.yili)

@dp.message(Reklama.holati)
async def reklama_holat_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon holatini to'g'ri kiriting ❗️")

   
@dp.message(F.text, Reklama.yili)
async def reklama_yili(message:Message,state:FSMContext):
    yili = message.text
    await state.update_data(yili=yili)
    await message.answer("Telefon rangini kiriting !")
    await state.set_state(Reklama.rang)

@dp.message(Reklama.yili)
async def reklama_yili_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Telefon yilini to'g'ri kiriting ❗️")



@dp.message(F.text,Reklama.rang)
async def reklama_rang(message:Message,state:FSMContext):
    rang = message.text
    await state.update_data(rang=rang)
    await message.answer("Telefon raqamingizni kiriting !", reply_markup=send_contact)
    await state.set_state(Reklama.tel)

@dp.message(Reklama.rang)
async def reklama_rang_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Telefon rangini to'g'ri kiriting ❗️")


@dp.message(F.contact | F.text.regexp( r"^(\+998|998)[0-9]{9}$"), Reklama.tel)
async def reklama_tel(message:Message,state:FSMContext):

    if message.contact:
        tel = message.contact.phone_number 
    else:
        tel = message.text

    await state.update_data(tel=tel)
    await message.answer("Telegramdagi foydalanuvchi nomingizni kiriting !", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reklama.tg_user)

@dp.message(Reklama.tel)
async def reklama_ism_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos telefon raqamini to'g'ri kiriting ❗️")


@dp.message(F.text, Reklama.tg_user)
async def reklama_user(message:Message,state:FSMContext):
    tg_user = message.text
    await state.update_data(tg_user=tg_user)
    await message.answer("Manzilingizni kiriting !")
    await state.set_state(Reklama.shahar)

@dp.message(Reklama.tg_user)
async def reklama_ism_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos foydalanuvchi nomingizni to'g'ri kiriting ❗️")



@dp.message(F.text, Reklama.shahar)
async def reklama_shahar(message:Message,state:FSMContext):
    data = await state.get_data()


    photo = data.get("photo")
    name = data.get("name")
    xotira = data.get("xotira")
    dakument = data.get("dakument")
    holat = data.get("holat")
    yili = data.get("yili")
    rang = data.get("rang")
    tel = data.get("tel")
    tg_user = data.get("tg_user")

    shahar = message.text
    user = message.from_user.id
    
    text = f"📱 {name}\n💾 {xotira}\n📦 {dakument}\n⚙️ {holat}\n📆 {yili}\n🌈 {rang}\n📞 {tel}\n🏙 {shahar}\n 👤 @{tg_user}\n🏷 {user}"

    await bot.send_photo(chat_id=ADMINS[0], photo=photo, caption=text, reply_markup=menu)

    await message.answer("Reklama adminga yuborildi qabul qilsa javob keladi !\n\nAgar siz yana telefoningizni reklama qilmoqchi bo'lsangiz  'Reklama berish'  tugmasini bosing.", reply_markup=yana)
    await state.clear()
    
@dp.callback_query(F.data == "True")
async def reklama_true(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    user = callbeck.message.caption.split()[-1]
    photo = callbeck.message.photo[-1].file_id
    text = callbeck.message.caption
    await bot.send_photo(chat_id=CHANNELS[0], photo=photo, caption=text)
    await bot.send_photo(chat_id=user, photo=photo, caption=text)    
    await bot.send_message(chat_id=user, text="✅\n\nSizni tabriklaymiz 🎉 sizning reklamangiz maqul keldi.Siz taqdim etgan reklamangiz endi reklamalar orasida !\nTez orada reklamangiz uchun buyurtma olasiz degan umiddamiz.Bizni tanlaganingiz uchun raxmat 🤖\nYana reklama yuborish uchun  'Reklama berish'  tugmasini bosing' tugmasini bosing.",reply_markup=yana)

@dp.callback_query(F.data == "False")
async def reklama_false(callbeck:Message,state:FSMContext):
    await callbeck.message.delete()
    photo = callbeck.message.photo[-1].file_id

    user = callbeck.message.caption.split()[-1] # Foydalanuvchi id
    text = callbeck.message.caption[:-12] # xabar id yo'q

    await bot.send_photo(chat_id=user, photo=photo, caption=text)
    await bot.send_message(chat_id=user, text="❌\n\nReklama maqul kelmadi.\nQayta reklamam yuborish uchun 'Reklama berish' - tugmasini bosing.\nBu safar ma'lumotlarni kiritishda ehtiyot bo'ling, faqat to'g'ri va mos keladigan ma'lumotlarni kiriting.\n🤖 Bu safargi reklamangiz yaxshi va to'liq bo'ladi degan umiddaman. ", reply_markup=yana)

@dp.message(F.text, Reklama.shahar)
async def reklama_shahar_del(message: Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos manzilingizni tug'ri kiriting ❗️")

















# agar erklama qoniqarli bo'lmasa foydalanuvchiga admin xabar yuborsin