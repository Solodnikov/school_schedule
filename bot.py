import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
# from config import settings
from handlers import start, callback
from dotenv import load_dotenv

load_dotenv()
# Теперь переменная BOT_TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

token = os.getenv('BOT_TOKEN',
                  default='6543904657:AAHgH0VgKygjxAKfbWldBxM9yMsAg-qvHx0')


async def main():
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=token,
        # token=settings.bot_token.get_secret_value(),
        parse_mode="HTML")
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_routers(start.router, callback.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# TODO: добавить убирание клавиатуры
# TODO: добавить различное повдение для разных класов
# (изначально для Миши и Маши)
# TODO: ? добавить время уроков
# TODO: запустить на сервере
# TODO: добавить выбор класса на старте и БД
