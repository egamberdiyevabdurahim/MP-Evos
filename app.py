import asyncio

from handlers.users import start, menu
from local_loeder import dp, bot, i18n
from main.database import database
from middlewares.languange import LanguageMiddleware
from utils.notify_devs import send_notification_to_devs
from utils.set_bot_commands import set_default_commands


async def main():
    await database.connect()
    # routes
    dp.include_router(router=start.router)
    dp.include_router(router=menu.router)

    # middleware
    dp.message.middleware(middleware=LanguageMiddleware(i18n=i18n))

    await dp.start_polling(bot)
    await set_default_commands(bot=bot)
    await send_notification_to_devs(bot=bot)


if __name__ == '__main__':
    print("Starting bot...")
    asyncio.run(main())
