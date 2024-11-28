from aiogram import Router, types, F
from loader import _

router = Router()

@router.message(F.text.in_(["Contact ☎️", "Aloqa ☎️", "Связаться ☎️"]))
async def contact_handler(message: types.Message):
    text = _("📲 Call center: 1112 or (71) 203-00-00")
    await message.answer(text=text)