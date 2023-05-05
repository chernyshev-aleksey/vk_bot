from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.database.user_city import get_city
from src.bot.keyboards.keyboards import get_menu_keyboard
from src.bot.misc.state import MenuStates
from src.config import state_dispenser
from src.services.weather import Weather

weather_labeler = BotLabeler()


@weather_labeler.message(state=MenuStates.weather_day, text=['Сегодня', 'сегодня'])
async def select_weather_today(message: Message):
    city = (await get_city(message.peer_id)).city
    w = Weather(city)
    await message.answer(w.get_message())


@weather_labeler.message(state=MenuStates.weather_day, text=['Завтра', 'завтра'])
async def select_weather_tomorrow(message: Message):
    city = (await get_city(message.peer_id)).city
    w = Weather(city, True)
    await message.answer(w.get_message())


@weather_labeler.message(state=MenuStates.weather_day, text=['Назад', 'назад'])
async def select_weather_back(message: Message):
    await state_dispenser.set(message.peer_id, MenuStates.menu)
    await message.answer('Ты находишься в меню', keyboard=get_menu_keyboard())


@weather_labeler.message(state=MenuStates.weather_day)
async def select_weather_any(message: Message):
    await message.answer('Принимаю только «Сегодня», «Завтра» или «Назад»')
