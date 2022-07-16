import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8334353"))
API_HASH = getenv("API_HASH", "4cf512e6f3274086dd6364a952b9a094")
BOT_USERNAME = getenv("BOT_USERNAME", "ADIBIKASHBOT")
BOT_TOKEN = getenv("BOT_TOKEN", "5428318094:AAGUmTK4Df2KGrU_-aKkUFhU1kxGEqOCscA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQAxCUW9wGIsJZPLX5qftii5QANAM8qXbuWpFaQQ4RO5cM9G9iuPRdyX6Q-ZgM64g3EySWb-jzzpKyafUS8nC9HoWz71aG7S8-cj8VzkeJJWz_Dh1V53-pA2yfs1eSnj0VIRLSVLhumL7VdCYXXB3tNNxua_bpqqjOG0G486Izt5_-Im_amUH2rhAOZ_uz0nNuc8EMYmgkd2yIZggxnKbd1j36AJ3TOBhYcHxZ7IWCtJ2Wjp-6tlzP8zSQsh5Vjy7zAhYRnlfLIY2i0rt3wprrZLl9aLe4H1gvksBXt767Y8_8C7SMx_dUsMsBWWUp2NxCqqMfSn2ZV6T8QGu93LIwmXAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
