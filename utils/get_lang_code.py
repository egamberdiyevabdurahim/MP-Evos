async def get_lang_by_text(language: str):
    if language == "Uzbek 🇺🇿":
        return "uz"
    elif language == "Russian 🇷🇺":
        return "ru"
    else:
        return "en"