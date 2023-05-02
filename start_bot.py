from vkbottle import Bot
from environs import Env

from src.bot.handlers.start import start_labeler
from src.config import state_dispenser, labeler, token

env = Env()
env.read_env('.env')

labeler.load(start_labeler)

bot = Bot(
    token=token,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()
