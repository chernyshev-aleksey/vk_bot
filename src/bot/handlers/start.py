from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.keyboards.kb import menu_kb, city_kb, begin_kb
from src.bot.misc.state import MenuStates
from src.config import state_dispenser, ctx_storage, token

start_labeler = BotLabeler()


@start_labeler.message(text="Начать")
async def start_handler(message: Message):
    # if message:
    #     await message.answer('Ты находишься в меню', keyboard=menu_kb)
    #     await state_dispenser.set(message.peer_id, MenuStates.menu)
    # else:
    users_info = await message.ctx_api.request("users.get", {
        'access_token': token,
        'user_ids': message.from_id,
        'fields': ['city']
    })
    if (city := users_info['response'][0]['city']['title']) is None:
        await message.answer("Пожалуйста, напиши свой город")
        await state_dispenser.set(message.peer_id, MenuStates.wait_city)
    else:
        await message.answer(f"Твой город - {city}, верно?", keyboard=city_kb)
        await state_dispenser.set(message.peer_id, MenuStates.confirm_city)
        ctx_storage.set('city', city)


@start_labeler.message(state=MenuStates.wait_city)
async def enter_city(message: Message):
    await message.answer(f'Твой город - {message.text}, верно?', keyboard=city_kb)
    await state_dispenser.set(message.peer_id, MenuStates.confirm_city)
    ctx_storage.set('city', message.text)


@start_labeler.message(state=MenuStates.confirm_city)
async def confirm_city(message: Message):
    if message.text.lower() == 'да':
        await message.answer(f'Город успешно зарегистрирован {ctx_storage.get("city")}', keyboard=begin_kb)
    elif message.text.lower() == 'нет':
        await message.answer('Пожалуйста, напиши свой город')
        await state_dispenser.set(message.peer_id, MenuStates.edit_city)
    else:
        await message.answer('Жду от тебя да или нет')