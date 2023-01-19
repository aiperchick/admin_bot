import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

from main import check_user_is_admin, check_words, ban_user, Test, process_done, shaurma, answer_q1, ham

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    load_dotenv()
    bot = Bot(os.getenv('MY_TOKEN'))
    dp = Dispatcher(bot)

    dp.register_message_handler(check_user_is_admin)
    dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!')
    executor.start_polling(dp, skip_updates=True)
    dp.register_message_handler(answer_q1, commands=['анкета'], commands_prefix='!')
    dp.register_message_handler(state=Test.Q1)
    dp.register_message_handler(state=Test.Q2)
    dp.register_message_handler(state=process_done)
    dp.register_message_handler(shaurma, commands=['shaurma'])
    dp.register_message_handler(ham, commands=['hamburger'])
    dp.register_message_handler(check_words)

