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
STRING_SESSION = getenv("STRING_SESSION", "BQBV_cPtAUA6xEsfMVZ-KRUTQI0ePT251LFTi81Rw4KF9XfFjaxTCvvLmpRDtb-5Ancet7BF17OSpoTNm-j3oco97YzvEgt9XVOS8OvR2k2Xcxd0LOSfCZeDiQwwvUNqKAFpcwtAM6eQTb437rIlBHiiQHvFVE7otVQYStWGKiJcatE81uGxlh8LEvLrht4bHF52a4ZaEx69KlookXPXoMKzUVrMuWsHTXXDQovU9jznyXdgrN9LHHeFwCVBSByljiYzxmuV4nzsXYHQXvOIIPqxwCZSqaC98KCbTHMLXR-q4VEaWEm7HRBhtjqRB9bDR2TCgknCVucCfgKTAOoCjsXeAAAAAHt4SIoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
aiohttpsession = aiohttp.ClientSession()
