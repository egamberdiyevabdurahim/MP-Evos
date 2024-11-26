from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from local_loeder import _


async def phone_number_share_keyboard(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("Share phone number ☎️", locale=language), request_contact=True)
        ]], resize_keyboard=True
    )
    return markup