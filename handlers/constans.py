import logging
from config import dp
from aiogram.utils import executor
from handlers import client, main

client.register_handlers_client(dp)
main.register_admin_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)