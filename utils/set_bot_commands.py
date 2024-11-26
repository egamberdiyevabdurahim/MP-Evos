from aiogram import types


async def set_default_commands(bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Start to use bot 🚀️️️️️️"),
            types.BotCommand(command="help", description="Find all features 🤖"),
            types.BotCommand(command="feedback", description="Send feedback to admin 📝"),
        ]
    )
