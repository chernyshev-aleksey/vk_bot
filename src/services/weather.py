import datetime
import json
import requests

from src.config import weather_token


class Weather:
    def __init__(self, city: str, tomorrow: bool = False):
        self.city = city
        self.tomorrow = tomorrow
        self.API_WEATHER = weather_token

    def get_message(self) -> str:
        rez = [f'Прогноз погоды в городе {self.city} {"на сегодня" if not self.tomorrow else "на завтра"}:\n']
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        headers = {"user-agent": USER_AGENT}
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&APPID={self.API_WEATHER}&units=metric&lang=ru',
            headers=headers)
        result = json.loads(response.text)
        for time in result['list']:
            if time['dt_txt'].split(' ')[0] == (datetime.datetime.today() + datetime.timedelta(days=(1 if self.tomorrow else 0))).strftime('%Y-%m-%d'):
                type_ = time['weather'][0]['main']
                if type_ == 'Clouds':
                    type_ = '☁️'
                elif type_ == 'Rain':
                    type_ = '🌧'
                elif type_ == 'Clear':
                    type_ = "☀️"

                time_ = time['dt_txt'].split(' ')[1]
                wind_ = str(time['wind']['speed']) + 'м/с'
                humidity_ = str(time['main']['humidity']) + '%'
                temp_ = str(time['main']['temp']) + '°C'

                rez.append(f"{time_[:-3]}{type_} {temp_} {wind_} {humidity_}")

        return '\n'.join(rez)
