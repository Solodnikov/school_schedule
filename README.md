# school_schedule

### телеграм-бот для получения расписания уроков в школе

# cuties_bot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Static Badge](https://img.shields.io/badge/aiogram-3.1.1.-greene)

### Описание проекта
Телеграм бот для получения расписания уроков. Бот определят текущую дату и предлагает ознакомиться с расписанием на ближайшие дни.

Пример развернутого доступен в телеграме: 
`@ClassMatrix_bot`


### Развертывание проекта

* клонируйте проект

   `https://github.com/Solodnikov/school_schedule.git`

* установите и запустите виртуальное окружение в папке проекта

    `python -m venv venv`

    `. venv/Scripts/activate`

* установите зависимости проекта

    `pip install -r requirements.txt`

### Запуск проекта

* создайте файл `.env` в корневой директории проекта:
    
    ```
    BOT_TOKEN='<ваш токен для бота>'
    ```
* запустить бота из корневой директории проекта
    
    `python bot.py`

* (альтернативный вариант запуска) запустить из докер контейнера

    `docker build -t <название образа> .`

    `docker run --name <название контейнера> -it <название образа>`
    