import config
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from NN import predict_from_binary

router = Router()


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Жду фото")


@router.message(Command("id"))
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


@router.message(F.photo)
async def echo_photo_message(msg: Message):
    photodata = msg.photo[-1].file_id
    file = await bot.get_file(photodata)
    file_path = file.file_path
    MyBinaryIO = await bot.download_file(file_path)
    prediction = predict_from_binary(MyBinaryIO)
    await msg.answer(f"Кажется {prediction[0]}, уверен на {prediction[1]}%")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    asyncio.run(main())
