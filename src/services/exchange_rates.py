import aiohttp

from bs4 import BeautifulSoup
from vkbottle import EMPTY_KEYBOARD
from vkbottle.bot import Message

from src.bot.keyboards.keyboards import get_menu_keyboard


async def get_rates(message: Message):
    search = await message.answer('Ищу курсы валют для тебя', keyboard=EMPTY_KEYBOARD)
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://www.google.com/search?q=курс+евро') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            euro = soup.find_all('span', {'class': ['SwHCTb']})[0].text
            await message.ctx_api.request("messages.delete", {
                'message_ids': [search.message_id], 'peer_id': message.from_id, 'delete_for_all': 1
            })
            await message.answer(f"Курс евро: {euro}₽")

        async with session.get(f'https://www.google.com/search?q=курс+доллара') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            dollar = soup.find_all('span', {'class': ['SwHCTb']})[0].text
            await message.answer(f"Курс доллара: {dollar}₽")

        async with session.get(f'https://www.google.com/search?q=курс+юаня') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            yuan = soup.find_all('span', {'class': ['SwHCTb']})[0].text
            await message.answer(f"Курс юаня: {yuan}₽")

        async with session.get(f'https://www.google.com/search?q=курс+тенге') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            tenge = soup.find_all('span', {'class': ['SwHCTb']})[0].text
            await message.answer(f"Курс тенге: {tenge}₽")

        async with session.get(f'https://www.google.com/search?q=курс+лиры') as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            lyre = soup.find_all('span', {'class': ['SwHCTb']})[0].text
            await message.answer(f"Курс лиры: {lyre}₽", keyboard=get_menu_keyboard())
