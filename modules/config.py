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
STRING_SESSION = getenv("STRING_SESSION", "BQBLj5_j627bjkEW-Xl6puO8SityckJq4Ja-EW2IcWyHcSrSsFJn9ovRjTIOAcrlFucz-CfSUfNjHSPv_aE_7dYxfWTtVi_GlzRzrS77oxPy3tCPq6FHVwEjmrPFYikYFKLqIhA0mJ6qSRQTcYqTQZ_PWiTslZNVE2v5r0BzygEnRM4d_zwj0SDNU5cDSAVHmQwY8N59lDgK68dLVhJknW348OWQH7s7Hd2UwOL8NsA-e8z5NNRnfVP-rk_VPUgyazqTzrO0tfVL6lRTmBOPEl7SSnbqKkF7vzSZxxeh-6oF4jqAobiAJcXxgzpsAXHp65HP-f4ASw5FcLMNndfRXTfnAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
