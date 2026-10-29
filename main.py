import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

# Токен берется из переменных окружения Render, либо можно указать ваш прямо здесь
BOT_TOKEN = os.getenv("BOT_TOKEN", "8797667876:AAF-8Tz9PpLlGnwSYnojM3GAcX52lIfOLWw")

# Текст приветствия, в точности повторяющий ваш скриншот
def get_welcome_text(chat_id: int, first_name: str) -> str:
    name = f", {first_name}" if first_name else ""
    return (
        f"👋 <b>Здравствуйте{name}!</b>\n\n"
        f"Это бот <b>MarketControl</b>. Он присылает сюда уведомления из игры: продажи и покупки в павильоне, SMS, звонки и нужды персонажа.\n\n"
        f"🆔 <b>Ваш Chat ID:</b>\n"
        f"{chat_id}\n"
        f"<i>Нажмите на число, чтобы скопировать.</i>\n\n"
        f"<b>Как подключить уведомления</b>\n"
        f"1. Откройте MarketControl → «Настройки» → «Настройки программы».\n"
        f"2. Вставьте Chat ID в блок Telegram и нажмите «Сохранить».\n"
        f"3. На вкладке «Обзор» включите переключатель.\n\n"
        f"Готово! Уведомления будут приходить в этот чат.\n"
        f"Если забудете свой ID, отправьте команду /id."
    )

async def start_handler(message: Message):
    text = get_welcome_text(message.chat.id, message.from_user.first_name)
    await message.answer(text, parse_mode="HTML")

async def id_handler(message: Message):
    text = get_welcome_text(message.chat.id, message.from_user.first_name)
    await message.answer(text, parse_mode="HTML")

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация команд
    dp.message.register(start_handler, Command(commands=["start", "help"]))
    dp.message.register(id_handler, Command(commands=["id"]))

    logging.basicConfig(level=logging.INFO)
    print("Бот MarketControl успешно запущен!")
    
    # Запуск через Long Polling (не требует вебхуков и белого IP)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())