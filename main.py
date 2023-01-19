from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from aiogram.dispatcher.filters.state import StatesGroup, State


async def check_user_is_admin(message: types.Message):
    """
    проверка на админа
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False


async def check_words(message: types.Message):
    """
    проверка плохих слов
    """
    BAD_WORDS = ['дурак', 'идиот']
    if message.chat.type != 'private':
        for i in BAD_WORDS:
            if i in message.text.lower().replace('', ''):
                await message.reply(
                    text=f"Пользователь {message.from_user.first_name} отправил"
                         f"запрещённое слово\n"
                         f"Админы удалять {message.from_user.first_name}: да/нет?")
                break


async def ban_user(message: types.Message):
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


async def answer_q1(message: types.Message):
    await Test.Q1.set()
    await message.answer("пожалйста ответье на вопросы снизу. эти вопросы нужны чтобы отправить ваш заказ.\n"
                         "вопрос №1\n"
                         "напишите ваше ФИО.")


async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    await Test.next()
    await message.reply("Введите ваш адресс")


async def process_done(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(
        "Спасибо. Мы с вами свяжемся.",
        reply_markup=ReplyKeyboardRemove()
    )


async def shaurma(message: types.Message):
    await message.answer_photo(
        open('./photo/arabskaja-shaurma.jpg', 'rb'),
        caption='сочная шаурма вам на стол, вкус арабской ночи.')


async def ham(message: types.Message):
    await message.answer_photo(
        open('./photo/hamburger.jpeg', 'rb'),
        caption='любите гамбургеры? тогда вам к нам!'
    )
