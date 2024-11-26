from aiogram import Router, F
from aiogram import types
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(F.text.in_(["Menu 🍕", "Menyu 🍕"]))
async def menu_handler(message: types.Message, state: FSMContext):
    text = "Menu menu"
    await message.answer(text=text)


@router.message(F.text.in_(["My orders 📖", "My buyurtmalarim 📖"]))
async def order_handler(message: types.Message, state: FSMContext):
    text = "Orders menu"
    await message.answer(text=text)


@router.message(F.text.in_(["Our branches 🏚", "Bizning filiallarimiz 🏚"]))
async def branch_handler(message: types.Message, state: FSMContext):
    text = "Branch menu"
    await message.answer(text=text)


@router.message(F.text.in_(["Contact ☎️", "Kontakt ☎️"]))
async def contact_handler(message: types.Message, state: FSMContext):
    text = "Contact menu"
    await message.answer(text=text)


@router.message(F.text.in_(["Settings ⚙️", "Sozlamalar ⚙️"]))
async def settings_handler(message: types.Message, state: FSMContext):
    text = "Settings menu"
    await message.answer(text=text)
