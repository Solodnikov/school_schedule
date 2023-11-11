from aiogram import Router, F
from aiogram.types import CallbackQuery
from schedule import schedule_1e
from keyboards import return_keyboard, start_keyboard
import datetime
from utils import get_date


router = Router()


@router.callback_query(F.data == 'main')
async def main(callback: CallbackQuery):
    day_today = datetime.datetime.today()
    await callback.message.answer(
        text=(
            f'{get_date(day_today)}\n\n'
            'Выбери что тебя интересует:'
        ),
    # await callback.message.answer(
    #     text='Выбери что тебя интересует:',
        reply_markup=start_keyboard(day_today).as_markup(),
    )


@router.callback_query(F.data == 'today')
async def today_schedule(callback: CallbackQuery):
    # получить день недели
    lessons_list = schedule_1e['monday']
    lessons = "\n".join(lessons_list)
    await callback.message.answer('Уроки сегодня:\n')
    await callback.message.answer(
        text=lessons,
        reply_markup=return_keyboard().as_markup(),
    )


@router.callback_query(F.data == 'tomorrow')
async def tomorrow_schedule(callback: CallbackQuery):
    # получить день недели
    lessons_list = schedule_1e['tuesday']
    lessons = "\n".join(lessons_list)
    await callback.message.answer('Уроки завтра:\n')
    await callback.message.answer(
        text=lessons,
        reply_markup=return_keyboard().as_markup(),
    )


# @router.callback_query(F.data == 'main')
# async def main(callback: CallbackQuery):
#     await callback.message.answer(
#         text='Выбери расписание на какой день тебя интересует:',
#         reply_markup=start_keyboard().as_markup(),
#     )
