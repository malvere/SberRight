import asyncio
import logging
import sys

from bot.src.start import start_bot, start_webhook
from web.plat import is_docker

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
if not is_docker():
    print("Using polling mode")
    bot = asyncio.run(start_bot())
else:
    print("Establishing webhook")
    bot = start_webhook()
