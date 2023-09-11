from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from keyboards import start_keyboard


router = Router()


def greeting_message(name):
    msg = (
        f"Привет {name}!\n"
        f"Тебя приветствует бот-помощник.\n"
        f"Я помогу тебе разобраться с расписанием уроков.\n"
        f"Что хочешь узнать?"
    )
    return msg


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        text=greeting_message('Незнакомец'),
        reply_markup=start_keyboard().as_markup(),
    )
