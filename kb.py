from vkbottle import Keyboard, KeyboardButtonColor, Text


KEYBOARD_STANDARD = Keyboard(one_time=False, inline=False)
KEYBOARD_STANDARD.add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
KEYBOARD_STANDARD.add(Text("Нет"), color=KeyboardButtonColor.NEGATIVE)
KEYBOARD_STANDARD = KEYBOARD_STANDARD.get_json()  # type: ignore


BEGIN_KEYBOARD = Keyboard(one_time=True, inline=False)
BEGIN_KEYBOARD.add(Text("Начать"), color=KeyboardButtonColor.PRIMARY)
BEGIN_KEYBOARD = BEGIN_KEYBOARD.get_json()

MAIN_MENU_KEYBOARD = Keyboard(one_time=False, inline=False)
MAIN_MENU_KEYBOARD.add(Text("Погода"), color=KeyboardButtonColor.PRIMARY)
MAIN_MENU_KEYBOARD.add(Text("Пробка"), color=KeyboardButtonColor.NEGATIVE)
MAIN_MENU_KEYBOARD.row()
MAIN_MENU_KEYBOARD.add(Text("Афиша"), color=KeyboardButtonColor.POSITIVE)
MAIN_MENU_KEYBOARD.add(Text("Валюта"), color=KeyboardButtonColor.SECONDARY)
MAIN_MENU_KEYBOARD = MAIN_MENU_KEYBOARD.get_json()


WEATHER_KEYBOARD = Keyboard(one_time=False, inline=False)
WEATHER_KEYBOARD.add(Text("Сегодня"), color=KeyboardButtonColor.PRIMARY)
WEATHER_KEYBOARD.add(Text("Завтра"), color=KeyboardButtonColor.NEGATIVE)
WEATHER_KEYBOARD = WEATHER_KEYBOARD.get_json()
