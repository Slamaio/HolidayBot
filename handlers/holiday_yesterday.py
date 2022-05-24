from aiogram import types

from parser import Parser
from config import URLs
from message_builder import MessageBuilder



async def cmd_holidayYesterday(message: types.Message):
    answer_text = MessageBuilder().message(URLs["yesterday"])

    inline_keyboard = types.InlineKeyboardMarkup()
    showMore_btn = types.InlineKeyboardButton(
        text="Показать больше праздников",
        callback_data="yesterday;1")
            
    inline_keyboard.add(showMore_btn)

    await message.reply(answer_text, reply_markup=inline_keyboard)