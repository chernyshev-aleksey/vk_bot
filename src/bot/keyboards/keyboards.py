from vkbottle import Keyboard, KeyboardButtonColor, Text


def get_city_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Нет"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard.get_json()


def get_begin_keyboard():
    keyboard = Keyboard(one_time=True, inline=False)
    keyboard.add(Text("Начать"), color=KeyboardButtonColor.PRIMARY)
    return keyboard.get_json()


def get_menu_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Погода"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Пробка"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Афиша"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Валюта"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Сменить город"), color=KeyboardButtonColor.SECONDARY)
    return keyboard.get_json()


def get_weather_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Сегодня"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Завтра"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard.get_json()


def get_afisha_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Сегодня"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Завтра"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard.get_json()


def get_settings_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Отмена"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard.get_json()


def get_settings_city_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("Нет"), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Отмена"), color=KeyboardButtonColor.SECONDARY)
    return keyboard.get_json()
