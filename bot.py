import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings
from handlers import start, callback


async def main():
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=settings.bot_token.get_secret_value(),
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
