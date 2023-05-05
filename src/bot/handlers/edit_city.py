from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.database.user_city import create_or_update
from src.bot.keyboards.keyboards import get_menu_keyboard, get_settings_keyboard, get_settings_city_keyboard
from src.bot.misc.state import MenuStates
from src.config import state_dispenser, ctx_storage

edit_city_labeler = BotLabeler()


@edit_city_labeler.message(state=MenuStates.setting_edit_city, text=['Отмена', 'отмена'])
async def setting_edit_city_cancel(message: Message):
    await state_dispenser.set(message.peer_id, MenuStates.menu)
    await message.answer('Ты находишься в меню', keyboard=get_menu_keyboard())


@edit_city_labeler.message(state=MenuStates.setting_edit_city)
async def setting_edit_city_any(message: Message):
    await message.answer(f'Твой город - {message.text}, верно?', keyboard=get_settings_city_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.setting_confirm_city)
    ctx_storage.set('city', message.text)


@edit_city_labeler.message(state=MenuStates.setting_confirm_city, text=['Да', 'да'])
async def setting_confirm_city_yes(message: Message):
    await create_or_update(message.peer_id, city := ctx_storage.get("city"))
    await message.answer(f'Город успешно зарегистрирован {city}', keyboard=get_menu_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.menu)


@edit_city_labeler.message(state=MenuStates.setting_confirm_city, text=['Нет', 'нет'])
async def setting_confirm_city_no(message: Message):
    await message.answer('Пожалуйста, напиши свой город', keyboard=get_settings_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.edit_city)


@edit_city_labeler.message(state=MenuStates.setting_confirm_city, text=['Отмена', 'отмена'])
async def setting_confirm_city_cancel(message: Message):
    await state_dispenser.set(message.peer_id, MenuStates.menu)
    await message.answer('Ты находишься в меню', keyboard=get_menu_keyboard())


@edit_city_labeler.message(state=MenuStates.setting_confirm_city)
async def setting_confirm_city_any(message: Message):
    await message.answer('Принимаю только «Да», «Нет» или «Отмена»')
