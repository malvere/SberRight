"""This file represent startup bot logic."""

from aiogram import Bot

from bot.config import conf

from .dispatcher import get_dispatcher


async def start_bot() -> Bot:
    """This function will start bot with polling mode."""
    print(conf.bot.token)
    bot = Bot(token=conf.bot.token)
    dp = get_dispatcher()
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )
    return bot