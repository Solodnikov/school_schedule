from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
import datetime


def greeting_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Давай посмотрим расписание",
            callback_data='main'),
        )
    return builder


def start_keyboard(day_today: datetime.datetime) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    # получаю день недели
    weekday = day_today.today().weekday()

    # формирую клавиатуру рабочих дней
    if weekday <= 3:
        builder.row(
            InlineKeyboardButton(
                text="Расписание на сегодня",
                callback_data=f'shedule {weekday}'),
        )
        builder.row(
            InlineKeyboardButton(
                text="Расписание на завтра",
                callback_data=f'shedule {weekday+1}'),
        )
    if weekday == 4:
        builder.row(
            InlineKeyboardButton(
                text="Расписание на сегодня",
                callback_data=f'shedule {weekday}'),
        )
    # формирую клавиатуру для выходного дня
    elif weekday == 5:
        builder.row(
            InlineKeyboardButton(
                text="Расписание на послезавтра",
                callback_data='shedule 0'),
        )
    elif weekday == 6:
        builder.row(
            InlineKeyboardButton(
                text="Расписание на завтра",
                callback_data='shedule 0'),
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
