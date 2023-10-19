import logging
import sys

# from aiogram import LoggingMiddleware
from aiogram import BaseMiddleware, Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.config import conf

router = Router()
@router.message(CommandStart())
async def cmd_start_handler(msg: Message) -> None:
    return await msg.answer('Hello!')

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(conf.webhook.webhook_host)

def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token="Hello",
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
    
