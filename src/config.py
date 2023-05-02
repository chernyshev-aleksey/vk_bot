from vkbottle import BuiltinStateDispenser, CtxStorage
from vkbottle.bot import BotLabeler
from environs import Env


env = Env()
env.read_env('.env')

token = env.str("BOT_TOKEN")
ctx_storage = CtxStorage()
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
weather_token = env.str("WEATHER_TOKEN")
