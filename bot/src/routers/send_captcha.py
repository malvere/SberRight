"""This file represents a start logic."""


from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from web import web_driver

captcha_router = Router(name='captcha')


@captcha_router.message(Command(commands='captcha'))
async def captcha_handler(msg: types.Message, command: CommandObject):
    """Help command handler."""
    if command.args != None:
        cpt = web_driver.captcha()
        await cpt.send_keys_to_captcha(command.args)
        await cpt.submit()
        await web_driver.parse_loaded()
        await msg.reply(text=f"Sent keys: {command.args}")
    else:
        cpt = web_driver.captcha()
        await cpt.screenshot()
        f = types.FSInputFile('test.png')
        await msg.reply_photo(photo=f, caption="Captcha: ")
