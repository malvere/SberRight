"""This file represent startup bot logic."""

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.config import conf

from .dispatcher import get_dispatcher


async def start_bot() -> Bot:
    """This function will start bot with polling mode."""
    bot = Bot(token=conf.bot.token)
    dp = get_dispatcher()
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )
    return bot

async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(conf.webhook.webhook_host)

def start_webhook() -> Bot:
    dp = get_dispatcher()

    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )

    webhook_requests_handler.register(
        app, 
        path=conf.webhook.webhook_url_path,
    )

    setup_application(app, dp, bot=bot)
    web.run_app(
        app, 
        host=conf.web_app.web_app_host, 
        port=conf.web_app.web_app_port,
    )
    return bot