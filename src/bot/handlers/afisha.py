from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.database.user_city import get_city
from src.bot.keyboards.keyboards import get_menu_keyboard
from src.bot.misc.state import MenuStates
from src.config import state_dispenser
from src.services.afisha import get_afisha


afisha_labeler = BotLabeler()


@afisha_labeler.message(state=MenuStates.afisha_day, text=['Сегодня', 'сегодня'])
async def select_afisha_today(message: Message):
    city = (await get_city(message.peer_id)).city
    await get_afisha(city, True, message)


@afisha_labeler.message(state=MenuStates.afisha_day, text=['Завтра', 'завтра'])
async def select_afisha_tomorrow(message: Message):
    city = (await get_city(message.peer_id)).city
    await get_afisha(city, False, message)


@afisha_labeler.message(state=MenuStates.afisha_day, text=['Назад', 'назад'])
async def select_afisha_back(message: Message):
    await state_dispenser.set(message.peer_id, MenuStates.menu)
    await message.answer('Ты находишься в меню', keyboard=get_menu_keyboard())


@afisha_labeler.message(state=MenuStates.afisha_day)
async def select_afisha_any(message: Message):
    await message.answer('Принимаю только «Сегодня», «Завтра» или «Назад»')
