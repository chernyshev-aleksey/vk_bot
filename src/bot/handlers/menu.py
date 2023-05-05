from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.database.user_city import get_city
from src.bot.keyboards.keyboards import get_weather_keyboard, get_settings_keyboard, get_afisha_keyboard
from src.bot.misc.state import MenuStates
from src.config import state_dispenser
from src.services.exchange_rates import get_rates
from src.services.traffic import get_traffic

menu_labeler = BotLabeler()


@menu_labeler.message(state=MenuStates.menu, text=['Погода', 'погода'])
async def menu_weather(message: Message):
    await message.answer('Выбери день', keyboard=get_weather_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.weather_day)


@menu_labeler.message(state=MenuStates.menu, text=['Пробка', 'пробка'])
async def menu_weather(message: Message):
    city = (await get_city(message.peer_id)).city
    await get_traffic(city, message)


@menu_labeler.message(state=MenuStates.menu, text=['Афиша', 'афиша'])
async def menu_weather(message: Message):
    await message.answer('Выбери день', keyboard=get_afisha_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.afisha_day)


@menu_labeler.message(state=MenuStates.menu, text=['Валюта', 'валюта'])
async def menu_weather(message: Message):
    await get_rates(message)


@menu_labeler.message(state=MenuStates.menu, text=['Сменить город'])
async def settings(message: Message):
    await message.answer('Напиши город, который хочешь установить', keyboard=get_settings_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.setting_edit_city)


@menu_labeler.message(state=MenuStates.menu)
async def menu_any(message: Message):
    await message.answer('Принимаю только «Погода», «Пробка», «Афиша», «Валюта» или «Сменить город»')
