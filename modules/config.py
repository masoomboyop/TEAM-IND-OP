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
STRING_SESSION = getenv("STRING_SESSION", "BQB393iCPxLoQUvHnaVTt4IZxAQU1n_Enn01F_LzIsFHJqTDGd9Ft5_tJuRWAMSNeJ4cwgqRr7aUn1HNY-6N59-DLSm0T0UDORkCB9TUj6hnJH7D1Th9g2uMXRyQn-XXKCCiL6C6PuCOlj5P8HW6rfkpQ6auyb1foi9plASByI5rltHwVyvZS1Eb7mHG2W7p461bs1-aT1Prkwn-3m5mSstTkRj3HBGg4aMPC0VbyIrx8x3lFx_7ohUlgS2F6PFzwYYDncQeI-8bSYthvBt2yVUJ0H-N1DcT1Yd7eCjk8VhSXJGfRSevw9HiVunJ8gr0LlpjOTVvga2yk3R5HJ6h7AcmAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
