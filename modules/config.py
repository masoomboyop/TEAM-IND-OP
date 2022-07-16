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
STRING_SESSION = getenv("STRING_SESSION", "BQBIsSK7H-4YFExba-5YQpf6Zz4kGn6QsoSnw8nBbsxGOM38-6wUtgrDH9nc9L0oJuvimoM8vjsUTdTtbYcDTrxKKlcmcJh-eAWaHQWp5xZjbXw9adLXqaxqyAzf1PFlKkGV_jfDL9bcB55jQyOy7mbMK8oQUTXS1cPnX-qcD9cUhBa0lXOU40B-Xdyv2BxR6-bnmX1b-MbkIgdQ_tEbK65Rna1BmVGCieTNQ-O8ZpLGG6yWjd6_qBiw3NiE-UjP3M1koAq75K1eh--uNXg0XPZhKxM5l42eWbEa6xzXu4BikCGWXMrqd-90Ts18oVQWdhxm7-LDlp8nJboKicwsOjHiAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
