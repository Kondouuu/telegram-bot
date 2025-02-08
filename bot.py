pip install aiogram googletrans==4.0.0-rc1
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from googletrans import Translator

# Укажите токен вашего бота
TOKEN = "7867988104:AAEvvPMuVqYM3t06st5Q4D2nMCYk__G29mA"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Привет! Отправь мне текст на русском, и я переведу его на казахский 🇰🇿.")

@dp.message_handler()
async def translate_text(message: Message):
    translated = translator.translate(message.text, src="ru", dest="kk")
    await message.reply(f"Перевод: {translated.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
