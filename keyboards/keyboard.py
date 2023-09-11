from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def start_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Расписание на сегодня", callback_data='today'),
    )
    builder.row(
        InlineKeyboardButton(
            text="Расписание на завтра", callback_data='tomorrow'),
    )
    return builder


def return_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Вернуться в главное меню",
            callback_data='main'),
    )
    return builder
