"""This file represents a start logic."""


from aiogram import Router, types
from aiogram.filters import Command

from web import web_driver

close_driver_router = Router(name='close-driver')


@close_driver_router.message(Command(commands='close'))
async def close_driver_handler(message: types.Message):
    """Help command handler."""
    await web_driver.grace_shutdown()
    return await message.answer('Driver closed')