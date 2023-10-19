import asyncio
import logging
import sys

from bot.src.start import start_bot

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
bot = asyncio.run(start_bot())
