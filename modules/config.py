import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11210087"))
API_HASH = getenv("API_HASH", "ba1d69a14f922e4025bfdd67139f35f1")
BOT_USERNAME = getenv("BOT_USERNAME", "ADIBIKASHBOT")
BOT_TOKEN = getenv("BOT_TOKEN", "5091185777:AAEjNy2ac11WTfKvFiCUup2WXN7SJitJO38")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQDEMbP_9Xz8djkUmD3eijhi6tMRMxbKgFgQAQ3vjO6fN-6nPAs3f_Qr4RvXlTbi7QEl6HOBRlcxKxNyVttMKWTWOzb88qrBE-wI-pk70Q1PBAi7UJ5Md_XItAILzpAIVsSgF20oO8fXkoyepwgs2X-mXssBbfWCZoldByKqMTgHQAdv-PZHOlbKVKXsr2T7TBRy_pB2oxnuXKbV5oieqjC_-60jW0LuAC4QZ9Pn9HvSjjE2tRgWbpecKngvS55YSzpF6UzlykLIvlv0709nAqKhqQh9FOXYGaGID3WogRKniMidcsStvscZ_TRlwtEv4caMV9VjKLA7xTWNr4t2rss6AAAAASwVnR4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1439222689 1282754256 5058237367 702821224 5168642497").split()))
aiohttpsession = aiohttp.ClientSession()
