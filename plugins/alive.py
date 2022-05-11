import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b559b922fe86fc0ab2285.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🐯 Hҽʅʅσ, I αɱ Sυρҽɾϝαʂƚ Hιɠԋ Qυαʅιƚყ 
Nσ Lαɠ Vƈ Mυʂιƈ Pʅαყҽɾ Bσƚ.

┏━━━━━━━━━━━━━━━━━┓
┣★ Cɾҽαƚσɾ 🛠️  [Bιƙαʂԋ Hαʅԃҽɾ](https://t.me/BikashHalder)
┣★ Cɾҽαƚσɾ 🛠️ [Aԃιƚყα Hαʅԃҽɾ](https://t.me/AdityaHalder)
┣★ Uρԃαƚҽʂ 📢 [Bɠƚ Bɾαɳԃ](https://t.me/BikashGedgetsTech)
┣★ Sυρρσɾƚ ☣️ [Bɠƚ Cԋαƚ](https://t.me/Bgt_chat)
┣★ Cԋαƚƚιɳɠ ©️ [Bɠƚ Cԋαƚ](https://t.me/adityadiscus)
┗━━━━━━━━━━━━━━━━━┛

🗽 Jυʂƚ Aԃԃ Mҽ » Tσ Yσυɾ Gɾσυρ Aɳԃ
Eɳʝσყ Bҽʂƚ Qυαʅιƚყ ❥︎ Mυʂιƈ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aԃԃ Mҽ Tσ Yσυɾ Gɾσυρ ❱ ➕", url=f"https://t.me/dotvcrobot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/start@dotvcrobot", "/alive", "/BGT",  ".Kaal"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b559b922fe86fc0ab2285.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Jσιɳ Oυɾ Cԋαƚ Gɾσυρ  🗽", url=f"https://t.me/BGT_CHAT")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "Bikash", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b559b922fe86fc0ab2285.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Cʅιƈƙ Mҽ Tσ Gҽƚ Rҽρσ 🗽", url=f"https://t.me/BikashHalder")
                ]
            ]
        ),
    )
