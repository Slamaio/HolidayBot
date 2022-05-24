from aiogram import types

from message_builder import MessageBuilder
from config import URLs


async def callbackHandler(callback_query: types.CallbackQuery):
    data = callback_query.data.split(";")

    url = URLs[data[0]]
    level = int(data[1])

    edited_text = f"{callback_query.message.text}\n\n{MessageBuilder().holidays(url, level)}"
    await callback_query.message.edit_text(edited_text)