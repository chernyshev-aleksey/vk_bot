from vkbottle import Keyboard, KeyboardButtonColor, Text


city_kb = Keyboard(one_time=False, inline=False)
city_kb.add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
city_kb.add(Text("Нет"), color=KeyboardButtonColor.NEGATIVE)
city_kb = city_kb.get_json()

begin_kb = Keyboard(one_time=True, inline=False)
begin_kb.add(Text("Начать"), color=KeyboardButtonColor.PRIMARY)
begin_kb = begin_kb.get_json()

menu_kb = Keyboard(one_time=False, inline=False)
menu_kb.add(Text("Погода"), color=KeyboardButtonColor.POSITIVE)
menu_kb.add(Text("Пробка"), color=KeyboardButtonColor.POSITIVE)
menu_kb.row()
menu_kb.add(Text("Афиша"), color=KeyboardButtonColor.POSITIVE)
menu_kb.add(Text("Валюта"), color=KeyboardButtonColor.POSITIVE)
menu_kb.row()
menu_kb.add(Text("Настройки⚙️"), color=KeyboardButtonColor.SECONDARY)
menu_kb = menu_kb.get_json()


weather_kb = Keyboard(one_time=False, inline=False)
weather_kb.add(Text("Сегодня"), color=KeyboardButtonColor.POSITIVE)
weather_kb.add(Text("Завтра"), color=KeyboardButtonColor.POSITIVE)
weather_kb.row()
weather_kb.add(Text("Назад"), color=KeyboardButtonColor.NEGATIVE)
weather_kb = weather_kb.get_json()
