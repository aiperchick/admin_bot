from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher


class Form(StatesGroup):
    Q1 = State()
    Q2 = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    """
    функция ошибки
    """
    current_state = await state.get_state()
    if current_state is None:
        return await state.finish()
    await message.reply(
        'Отмена', reply_markup=types.ReplyKeyboardRemove())


async def form_start(message: types.Message):
    """
    начало fsm, первый впорос
    """
    await Form.Q1.set()
    await message.answer("пожалйста ответье на вопросы снизу. эти вопросы нужны чтобы отправить ваш заказ.\n"
                         "вопрос №1\n"
                         "напишите ваше ФИО.")


async def process_name(message: types.Message, state: FSMContext):
    """
    обрабатываем первый вопрос, задаем второй вопрос
    """
    async with state.proxy() as data:
        data['Q1'] = message.text
        print(data)

    await Form.next()
    await message.reply("Введите ваш адресс")


async def process_adresse(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q2'] = message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.answer(
        f"""Подтвердите ваши данные:фио: {data['Q1']}адресс: {data['Q2']} Все верно?""",
        reply_markup=yes_no_kb)


async def process_done(message: types.Message, state: FSMContext):
    """
    обрабатываем вопрос
    """
    await state.finish()
    await message.reply(
        "Спасибо. Мы с вами свяжемся.",
        reply_markup=ReplyKeyboardRemove()
    )


async def shaurma(message: types.Message):
    """
    фотографие и описание
    """
    await message.answer_photo(
        open('./photo/arabskaja-shaurma.jpg', 'rb'),
        caption='сочная шаурма вам на стол, вкус арабской ночи.')


async def ham(message: types.Message):
    """
    фотографие и описание
    """
    await message.answer_photo(
        open('./photo/hamburger.jpeg', 'rb'),
        caption='любите гамбургеры? тогда вам к нам!'
    )
