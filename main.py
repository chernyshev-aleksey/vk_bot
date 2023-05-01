from vkbottle import BaseStateGroup
from vkbottle.bot import Bot, Message

from kb import KEYBOARD_STANDARD, BEGIN_KEYBOARD, MAIN_MENU_KEYBOARD, WEATHER_KEYBOARD
from src.weather.weather import Weather

bot = Bot(token="vk1.a.-Zqo42cGtcQMXAGcq99JIxv4wIsbZHh-2koqStCZBu-CayMFE3bdj2--YiCfW-JuwgW86HtmoAO6liSpF8Jr0VVhKFDK7hNbhF6TshIcYNj8YiwHwwPtb3LUtFsEgsfWpHK0ao1zCPRqaBZsByFkE7CpIMW8D0VRi21V9BAjtqRcsEqQGXuaCGyUcpx1jdD4eCFh9IFKsVitujrMGqJKLA")


class MenuStates(BaseStateGroup):
    CONFIRM_CITY_STATE = "CONFIRM_CITY_STATE"
    EDIT_CITY_STATE = "EDIT_CITY_STATE"
    MENU_STATE = "MENU_STATE"
    WEATHER_DAY_STATE = "WEATHER_DAY_STATE"


@bot.on.message(text="Начать")
async def hi_handler(message: Message):
    if message:
        await message.answer('Ты находишься в меню', keyboard=MAIN_MENU_KEYBOARD)
        await bot.state_dispenser.set(message.peer_id, MenuStates.MENU_STATE)
    else:
        users_info = await bot.api.users.get(message.from_id, fields=['city'])
        print(users_info)
        if (city := users_info[0].city) is None:
            await message.answer("Пожалуйста, напиши свой город")
        else:
            await message.answer(f"Твой город - {city.title}, верно?", keyboard=KEYBOARD_STANDARD)
            await bot.state_dispenser.set(message.peer_id, MenuStates.CONFIRM_CITY_STATE)


@bot.on.message(state=MenuStates.CONFIRM_CITY_STATE)
async def confirm_city(message: Message):
    if message.text.lower() == 'да':
        await message.answer('Город успешно зарегистрирован', keyboard=BEGIN_KEYBOARD)
    elif message.text.lower() == 'нет':
        await message.answer('Пожалуйста, напиши свой город')
        await bot.state_dispenser.set(message.peer_id, MenuStates.EDIT_CITY_STATE)
    else:
        await message.answer('Жду от тебя да или нет')


@bot.on.message(state=MenuStates.MENU_STATE)
async def menu(message: Message):
    if message.text.lower() == 'погода':
        await message.answer('Выбери день', keyboard=WEATHER_KEYBOARD)
        await bot.state_dispenser.set(message.peer_id, MenuStates.WEATHER_DAY_STATE)
    elif message.text.lower() == 'пробка':
        await message.answer('Пробка')
    elif message.text.lower() == 'афиша':
        await message.answer('афиша')
    elif message.text.lower() == 'валюта':
        await message.answer('Валюта')


@bot.on.message(state=MenuStates.WEATHER_DAY_STATE)
async def select_weather(message: Message):
    if message.text.lower() == 'сегодня':
        city = 'Казань'
        w = Weather(city)
        await message.answer(w.get_message())
    elif message.text.lower() == 'завтра':
        city = 'Казань'
        w = Weather(city, True)
        await message.answer(w.get_message())

bot.run_forever()
