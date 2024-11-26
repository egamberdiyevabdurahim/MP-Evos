from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from local_loeder import _

languages_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbek 🇺🇿"),
            KeyboardButton(text="Russian 🇷🇺"),
            KeyboardButton(text="English 🇺🇸"),
        ]
    ], resize_keyboard=True
)


async def user_main_menu_keyboard_with_lang(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍕", locale=language))
            ],
            [
                KeyboardButton(text=_("My orders 📖", locale=language)),
                KeyboardButton(text=_("Our branches 🏚", locale=language)),
            ],
            [
                KeyboardButton(text=_("Contact ☎️", locale=language)),
                KeyboardButton(text=_("Settings ⚙️", locale=language)),
            ]
        ], resize_keyboard=True
    )

    return markup
