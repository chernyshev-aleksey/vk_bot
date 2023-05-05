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

from src.bot.keyboards.keyboards import get_afisha_keyboard


async def get_afisha(city, today: bool, message: Message):
    search = await message.answer('Ищу для тебя мероприятия...', keyboard=EMPTY_KEYBOARD)
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://www.google.com/search?q=афиша+ру+{city}+сегодня') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            city_link = str(soup.find_all('div', 'MjjYud')[0].find_all('a')[0]['href'])
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options)
            driver.get(city_link)
            await asyncio.sleep(1)
            page = 0 if today else 1
            try:
                driver.find_elements(By.CLASS_NAME, 'qaeyi')[page].click()
                await asyncio.sleep(1)
                res = driver.find_elements(By.CLASS_NAME, 'wsXlA.pZeTF.SUiYd')
                numb = 1
                await message.ctx_api.request("messages.delete", {
                    'message_ids': [search.message_id], 'peer_id': message.from_id, 'delete_for_all': 1
                })
                for i in res:
                    if numb > 5:
                        continue
                    try:
                        price = i.find_elements(By.CLASS_NAME, 'Ef2IR.jEnBm')[0].text
                    except IndexError:
                        pass
                    else:
                        if 'От' in price:
                            name = i.find_elements(By.CLASS_NAME, 'vcSoT.b6DKO')[0].text
                            link = i.find_elements(By.CLASS_NAME, 'vcSoT.dcsqk')[0].get_attribute('href')
                            await message.answer(f'{name}\n{price}\n{link}', dont_parse_links=True,
                                                 keyboard=get_afisha_keyboard())
                            numb += 1

                if numb == 1:
                    await message.answer('Мероприятия не найдены :(', keyboard=get_afisha_keyboard())

            except IndexError:
                await message.answer('Мероприятия не найдены :(', keyboard=get_afisha_keyboard())

            finally:
                driver.close()
