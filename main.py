import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart , Command
from aiogram.types import Message

from py import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("assalomu alaykum , nima gap")

@dp.message(Command("salom"))
async def cmd_salom(message: Message):
    await message.reply("salomu alaykum , nima gap")

@dp.message(F.text == "na gap")
async def cmd_na_gap(message: Message):
    await message.reply("yaxhi ozingizda nima gap")

@dp.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f"Foto ID si: {message.photo[1].file_id}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())