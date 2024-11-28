from aiogram import Router, types, F

from loader import _
from keyboards.default.user import settings_menu, user_main_menu_keyboard

router = Router()

@router.message(F.text.in_("Settings ⚙️"))
async def settings_handler(message: types.Message):
    await message.reply(text=_("Settings menu:"), reply_markup=settings_menu)


@router.message(F.text.in_("Change Language 🌍"))
async def change_language_handler(message: types.Message):
    await message.reply(text=_("Language options:\n1️⃣ English\n2️⃣ Russain\n3️⃣ O'zbekcha"))


@router.message(F.text.in_("Go Back 🔙"))
async def go_back_handler(message: types.Message):
    await message.reply(text=_("Returning to the main menu:"), reply_markup=user_main_menu_keyboard)
