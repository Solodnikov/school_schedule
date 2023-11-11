import datetime

DAYS_NAME = (
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье',
)

MONTHS_NAME = {
    1: 'Января',
    2: 'Февраля',
    3: 'Марта',
    4: 'Апреля',
    5: 'Мая',
    6: 'Июня',
    7: 'Июля',
    8: 'Августа',
    9: 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря',
}


def get_date(day_today: datetime.datetime) -> str:
    # получаю день недели
    day_today = datetime.datetime.today()
    month_name = MONTHS_NAME[day_today.month]
    weekday_name = DAYS_NAME[day_today.weekday()]

    return (
        f'Сегодня {weekday_name}, {day_today.day} {month_name}'
    )
