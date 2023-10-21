import logging
import sys

# from aiogram import LoggingMiddleware
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.config import conf

from .dispatcher import get_dispatcher


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(conf.webhook.webhook_host)

def main() -> None:
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
    
