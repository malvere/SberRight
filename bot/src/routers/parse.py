"""This file represents a start logic."""
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from web import web_driver

parse_loaded_router = Router(name='parse-loaded')


@parse_loaded_router.message(Command(commands='parse'))
async def init_handler(message: types.Message):
    """Captcha handler."""
    try:
        print("First attempt...")
        await web_driver.parse_loaded()
        return await message.answer("Finished")
    except:
        print("First attempt failed. Waiting for captcha")
        cpt = web_driver.captcha()
        await cpt.screenshot()
        print("First try")
        f = FSInputFile("test.png")
        return await message.answer_photo(photo=f, caption="captcha detected!")
    