


@start_labeler.message(state=MenuStates.menu)
async def menu(message: Message):
    if message.text.lower() == 'погода':
        await message.answer('Выбери день', keyboard=weather_kb)
        await state_dispenser.set(message.peer_id, MenuStates.weather_day)
    elif message.text.lower() == 'пробка':
        await message.answer('Пробка')
    elif message.text.lower() == 'афиша':
        await message.answer('афиша')
    elif message.text.lower() == 'валюта':
        await message.answer('Валюта')


@start_labeler.message(state=MenuStates.weather_day)
async def select_weather(message: Message):
    if message.text.lower() == 'сегодня':
        city = 'Казань'
        w = Weather(city)
        await message.answer(w.get_message())
    elif message.text.lower() == 'завтра':
        city = 'Казань'
        w = Weather(city, True)
        await message.answer(w.get_message())
    elif message.text.lower() == 'назад':
        await state_dispenser.set(message.peer_id, MenuStates.menu)
        await message.answer('Ты находишься в меню', keyboard=menu_kb)
