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
BOT_TOKEN = getenv("BOT_TOKEN", "5105047271:AAFceMfSKtM9lJ22nuwLKIu8vvtMC6vLW1o")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQARwjIVv5iggyJqnMT0lU6jUfQU9e5NP3LixFip-6hIxyWYcvxnO8sJL4hVmpILhG0IhzsqrN676Pt7dyU9V3XhFxQyMXIbOV71BmJi0Q96m-pRsYI-k_St5KXUGTcKeAj5XIbNshdTq6byP0yL5vv7m7Va-I-ua4kI-A7VL0qTaZncuJ3qzszcV_mbTWQNchOI6DFverrHoWtinMdaPWJp1D4RrsRgK87zxBDlGylhHbkbQnmG_n-C4KXeQfEt10bClGZk3wWPxsONvbjgt_o4kXgsuPyKHr450hAERulUOa3IJfQekALIhWTZyVZzRoIPIqvnVMFoJVZx4MDdyrATAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
