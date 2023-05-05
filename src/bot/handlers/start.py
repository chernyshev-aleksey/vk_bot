from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler

from src.bot.database.user_city import db, create_or_update, get_city
from src.bot.keyboards.keyboards import get_menu_keyboard, get_city_keyboard, get_begin_keyboard
from src.bot.misc.state import MenuStates
from src.config import state_dispenser, ctx_storage, token

start_labeler = BotLabeler()


@start_labeler.message(text="Начать")
async def start_handler(message: Message):
    user = await get_city(message.peer_id)
    if user:
        await message.answer(f'Меню\n\nВыбранный город: {user.city}', keyboard=get_menu_keyboard())
        await state_dispenser.set(message.peer_id, MenuStates.menu)

    else:
        try:
            city = (await message.ctx_api.request("users.get", {
                'access_token': token, 'user_ids': message.from_id, 'fields': ['city']
            }))['response'][0]['city']['title']
        except KeyError:
            await message.answer("Пожалуйста, напиши свой город")
            await state_dispenser.set(message.peer_id, MenuStates.wait_city)
        else:
            if city is None:
                await message.answer("Пожалуйста, напиши свой город")
                await state_dispenser.set(message.peer_id, MenuStates.wait_city)
            else:
                await message.answer(f"Твой город - {city}, верно?", keyboard=get_city_keyboard())
                await state_dispenser.set(message.peer_id, MenuStates.confirm_city)
                ctx_storage.set('city', city)


@start_labeler.message(state=MenuStates.wait_city)
async def enter_city(message: Message):
    await message.answer(f'Твой город - {message.text}, верно?', keyboard=get_city_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.confirm_city)
    ctx_storage.set('city', message.text)


@start_labeler.message(state=MenuStates.confirm_city, text=['Да', 'да'])
async def confirm_city_yes(message: Message):
    await create_or_update(message.peer_id, city := ctx_storage.get("city"))
    await message.answer(f'Город успешно зарегистрирован {city}', keyboard=get_begin_keyboard())
    await state_dispenser.set(message.peer_id, MenuStates.menu)


@start_labeler.message(state=MenuStates.confirm_city, text=['Нет', 'нет'])
async def confirm_city_yes(message: Message):
    await message.answer('Пожалуйста, напиши свой город')
    await state_dispenser.set(message.peer_id, MenuStates.edit_city)


@start_labeler.message(state=MenuStates.confirm_city)
async def confirm_city_yes(message: Message):
    await message.answer('Жду от тебя да или нет :)')


@start_labeler.message(state=MenuStates.edit_city)
async def edit_city(message: Message):
    async with db.with_bind('postgresql://localhost/postgres'):
        city = message.text
        ctx_storage.set("city", city)
        await create_or_update(message.peer_id, city)
        await message.answer(f'Город успешно зарегистрирован "{city}"', keyboard=get_menu_keyboard())
