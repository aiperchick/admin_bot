from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging

from handlers import client, admin_bot
from handlers.admin_bot import check_user_is_admin, check_words, ban_user
from handlers.client import (Form,
                             cancel_handler,
                             form_start,
                             process_name,
                             process_adresse,
                             process_done,
                             )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    load_dotenv()
    bot = Bot(getenv('MY_TOKEN'))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(process_name, state=Form.Q1)
    dp.register_message_handler(process_adresse, state=Form.Q2)
    dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
    dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(process_adresse, commands=['да'], commands_prefix=['!'])
    dp.register_message_handler(check_words)

    executor.start_polling(dp, skip_updates=True)
