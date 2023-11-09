"""This file represents a start logic."""
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from web import web_driver

init_router = Router(name='init')


@init_router.message(Command(commands='init'))
async def init_handler(message: types.Message):
    """Captcha handler."""
    await web_driver.go_sber()
    await web_driver.create_context_page()
    # web_driver.raw_go()
    try:
        print("First attempt...")
        await web_driver.parse()
        # await web_driver.grace_shutdown()
        return await message.answer("First try!")
    except:
        print("First attempt failed. Waiting for captcha")
        
        cpt = web_driver.captcha()
        await cpt.screenshot()
        print("First try")
        f = FSInputFile("test.png")
        return await message.answer_photo(photo=f, caption="captcha detected!")
    