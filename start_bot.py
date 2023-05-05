from vkbottle import Bot
from environs import Env

from src.bot.handlers.afisha import afisha_labeler
from src.bot.handlers.edit_city import edit_city_labeler
from src.bot.handlers.menu import menu_labeler
from src.bot.handlers.start import start_labeler
from src.bot.handlers.weather import weather_labeler
from src.config import state_dispenser, labeler, token

env = Env()
env.read_env('.env')

labeler.load(start_labeler)
labeler.load(menu_labeler)
labeler.load(edit_city_labeler)
labeler.load(weather_labeler)
labeler.load(afisha_labeler)


bot = Bot(
    token=token,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()
