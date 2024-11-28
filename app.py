import asyncio

from loader import dp

from main.database import database


if __name__ == '__main__':
    dp.start_polling()
    asyncio.run(database.connect())
