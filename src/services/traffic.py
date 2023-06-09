import asyncio

import aiohttp
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from vkbottle import EMPTY_KEYBOARD
from vkbottle.bot import Message
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from src.bot.keyboards.keyboards import get_menu_keyboard


async def get_traffic(city, message: Message):
    search = await message.answer('Ищу ситуацию на дороге твоем городе...', keyboard=EMPTY_KEYBOARD)
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://www.google.com/search?q=яндекс+карты+{city}') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            city_link = str(soup.find_all('div', 'yuRUbf')[0].find_all('a')[0]['href'])
            city_link = city_link.split('/')
            city_link.insert(6, 'probki')
            city_link = '/'.join(city_link)

            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options)
            driver.get(city_link)
            await asyncio.sleep(5)
            res = driver.find_element(By.CLASS_NAME, 'traffic-raw-icon__text').text
            driver.close()
            await message.ctx_api.request("messages.delete", {
                'message_ids': [search.message_id], 'peer_id': message.from_id, 'delete_for_all': 1
            })
            await message.answer(f"В городе {city} {res} балла пробок", keyboard=get_menu_keyboard())
