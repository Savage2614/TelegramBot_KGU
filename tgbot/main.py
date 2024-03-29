from cgitb import text
import logging
from operator import contains
from re import IGNORECASE
from tracemalloc import stop
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from os import getenv
from sys import exit
import sqlite3

conn = sqlite3.connect('databases/subjects.db')
cur = conn.cursor()

# Объект бота
bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# StartCommand
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Список доступных комманд: \n/ru \n/kz \n/menu\nЧто бы не писать команды вручную, мы добавили "
                         "кнопку слева от клавиатуры. Нажав на нее вы сможете выполнять эти команды.\nТак же наш бот "
                         "поможет вам узнать информацию о том или ином профильном предмете. Для этого достаточно "
                         "нажать на соответвующую кнопку, или написать название предмета")


# Physic
@dp.message_handler(lambda message: 'физ' in message.text.lower())
@dp.message_handler(lambda message: 'физ' in message.text.lower() and '-' not in message.text.lower())
async def cmd_phys(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика", callback_data='phys_math'),
        types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# Math
@dp.message_handler(lambda message: 'мат' in message.text.lower())
@dp.message_handler(lambda message: 'мат' in message.text.lower() and '-' not in message.text.lower())
async def cmd_math(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика", callback_data='phys_math'),
        types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# Biology
@dp.message_handler(lambda message: 'био' in message.text.lower())
async def cmd_bio(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
        types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# Chemistry
@dp.message_handler(lambda message: 'хим' in message.text.lower())
async def cmd_chem(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem'),
        types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# Geography
@dp.message_handler(lambda message: 'гео' in message.text.lower())
async def cmd_geo(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
        types.InlineKeyboardButton(text="География-Всемирная История", callback_data='geo_hist'),
        types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng'),
        types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# History
@dp.message_handler(lambda message: 'истор' in message.text.lower())
async def cmd_history(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="География-Всемирная История", callback_data='geo_hist'),
        types.InlineKeyboardButton(text="Всемирная История-Человек.Общество.Право",
                                   callback_data='hist_hsl'),
        types.InlineKeyboardButton(text="Английский Язык-Всемирная История", callback_data='eng_hist'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# EnglishLanguage
@dp.message_handler(lambda message: 'англ' in message.text.lower())
async def cmd_eng_lang(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Английский Язык-Всемирная История", callback_data='eng_hist'),
        types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# RusLang
@dp.message_handler(lambda message: 'русс' in message.text.lower())
async def cmd_rus_lang(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Русский Язык-Русская Литература", callback_data='rulang_rulit'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# KZLang
@dp.message_handler(lambda message: 'казах' in message.text.lower())
async def cmd_kz_lang(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Казахский Язык-Казахская Литература", callback_data='kzlang_kzlit'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# HSL
@dp.message_handler(lambda message: 'человек' in message.text.lower() or 'чоп' in message.text.lower())
async def cmd_hsl(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Всемирная История-Человек.Общество.Право",
                                   callback_data='hist_hsl'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


# Payment
@dp.message_handler(Text(contains="плата", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    await message.answer('<b>Биология-География</b>\n "Педагогика и Психология" - 443.400 тг в год\n "',
                         parse_mode='html')


# Magistracy
@dp.message_handler(lambda message: 'магистр' in message.text.lower())
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["first", "second", "third", "chetvertyii",
               "pyatyi", "shestoi", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("👨🏻‍🎓Выберите специальность магистратуры👨🏻‍🎓", reply_markup=keyboard)


# Doctoral
@dp.message_handler(lambda message: 'доктор' in message.text.lower())
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["first1", "second2", "third3", "chetvertyii4",
               "pyatyi5", "shestoi6", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("👨‍🔬Выберите специальность докторантуры👨‍🔬", reply_markup=keyboard)


# GrantsAndDiscount
@dp.message_handler(lambda message: 'гранты' in message.text.lower() or 'скидки' in message.text.lower())
async def cmd_menu_items(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="100%", callback_data='100'),
        types.InlineKeyboardButton(text="50%", callback_data='50'),
        types.InlineKeyboardButton(text="25%", callback_data='25'),
        types.InlineKeyboardButton(text="20%", callback_data='20'),
        types.InlineKeyboardButton(text="10%", callback_data='10'),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Выберите скидку", reply_markup=keyboard)


# Specialties
@dp.message_handler(lambda message: 'специально' in message.text.lower())
async def cmd_menu_items(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="👨🏻‍🎓Магистратуры👨🏻‍🎓", callback_data='special_mag'),
        types.InlineKeyboardButton(text="👨‍🔬Докторантуры👨‍🔬", callback_data='special_doc'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите специальности:", reply_markup=keyboard)


@dp.message_handler(commands="menu")
async def cmd_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓",
               "👨‍🔬Специальности Докторантуры👨‍🔬", "🗺Узнать расположения корпусов🗺"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте, Коркыт Ата бот приветствует вас🙋‍♂️\nВыберите действие",
                         reply_markup=keyboard)


# Ask a Question
@dp.message_handler(lambda message: 'вопрос' in message.text.lower() or 'спрос' in message.text.lower())
async def cmd_ask_ques(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Напишите нам на WhatsApp", callback_data='100',
                                   url='http://wa.me/+77029224458'),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("<a href='http://wa.me/+77029224458'><b>Напишите нам на WhatsApp</b></a>", parse_mode='html',
                         reply_markup=keyboard)


# GeolocationButton
@dp.message_handler(lambda message: 'расположение' in message.text.lower() or 'корпус' in message.text.lower())
async def cmd_geolocation(message: types.Message):
    buttons = [

        types.InlineKeyboardButton(text="1 Корпус", url="https://goo.gl/maps/xp3VypLLNsuLW8jEA"),
        types.InlineKeyboardButton(text="2 Корпус", url="https://goo.gl/maps/QE1pecsT7p7PMK4C9"),
        types.InlineKeyboardButton(text="3 Корпус", url="https://goo.gl/maps/odS2XEjmiYBR8pp59"),
        types.InlineKeyboardButton(text="4 Корпус", url="https://goo.gl/maps/mwcpoZ4R3aFbUQ8j6"),
        types.InlineKeyboardButton(text="5 Корпус", url='https://goo.gl/maps/gFQ95qr8REu9uSNG6'),
        types.InlineKeyboardButton(text="6 Корпус", url="https://goo.gl/maps/VhMHUtxPmj5WuHTp8"),
        types.InlineKeyboardButton(text="7 Корпус", url="https://goo.gl/maps/DLXiX1NEzUNMWgd7A"),
        # types.InlineKeyboardButton(text="8 Корпус", url=""),
        types.InlineKeyboardButton(text="9 Корпус", url="https://goo.gl/maps/WLbZkTRML7vxcGR78"),
        types.InlineKeyboardButton(text="Главный Корпус", url='https://goo.gl/maps/AEezyGb9xuAkNqzW6'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer(text='Выберите корпус который вас интересует', reply_markup=keyboard)


# ItemsButton
@dp.message_handler(Text(contains="предметы", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, )
    buttons = ["Биология-География", "География-Всемирная История", "География-Английский",
               "Всемирная История-Человек.Общество.Право", "Казахский Язык-Казахская Литература", "Физика-Математика",
               "Математика-География", "Русский Язык-Русская Литература", "Химия-Биология",
               "Физика-Химия", "Английский Язык-Всемирная История", "Творческий экзамен", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("Выберите свои предметы", reply_markup=keyboard)


# BackButton
@dp.message_handler(Text(contains="назад", ignore_case=True))
async def cmd_back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓",
               "👨‍🔬Специальности Докторантуры👨‍🔬", "🗺Узнать расположения корпусов🗺"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте, Коркыт Ата бот приветствует вас🙋‍♂️\nВыберите действие",
                         reply_markup=keyboard)


def request(message):
    cur.execute(
        f"SELECT groups.nomer, groups.name, year_2020.grant, year_2020.jk, year_2020.ak FROM groups JOIN year_2020 ON "
        f"groups.nomer = year_2020.group_nomer WHERE groups.subject = '{message}' ORDER BY groups.nomer ASC;")
    data_groups = cur.fetchall()
    cur.execute(
        f"SELECT spec.group_nomer, spec.name FROM spec JOIN groups ON groups.nomer = spec.group_nomer WHERE subject = "
        f"'{message}' ORDER BY spec.group_nomer ASC;")
    data_spec = cur.fetchall()
    text = ''
    for group in data_groups:
        group = list(group)
        text = text + f"<{group[1]}>\n"
        for spec in data_spec:
            spec = list(spec)
            if spec[0] == group[0]:
                text = text + "-" + spec[1] + "-\n"  # подумай
        text = text + f"Бакалавриатқа бөлінген грант саны:{group[2]}\nЖалпы конкурс бойынша грантқа түскен минималды балл:{group[3]}\nАуылдық квотамен грантқа түскен минималды балл:{group[4]}\n\n"
    return text


@dp.message_handler(text="Математика-Физика")
async def math_fiz(message: types.message, call: types.callback_query):
    await message.answer(request(message.text))

@dp.message_handler()
async def txt_none(message: types.Message):
    await message.answer(text="Я не понимаю что вы написали🥶🥶🥶")
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
