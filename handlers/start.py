from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from keyboards.keyboard import (start_keyboard,
                                greeting_keyboard)
from utils import get_date
import datetime
from aiogram.types import FSInputFile
from constants import START_FOTO


router = Router()


def greeting_message(name):
    msg = (
        f"Привет {name}!\n"
        f"Тебя приветствует бот-помощник.\n"
        f"Я помогу тебе разобраться с расписанием уроков.\n"
    )
    return msg


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    photo = FSInputFile(START_FOTO)
    await message.answer_photo(photo)
    await message.answer(
        text=greeting_message('Незнакомец'),
        reply_markup=greeting_keyboard().as_markup(),
    )
