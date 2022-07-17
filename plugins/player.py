# Bikash Halder // @BikashHalder @AdityaHalder

import os
import aiofiles
import aiohttp
import ffmpeg
import random
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import DURATION_LIMIT, que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

# plus
chat_id = None
useer = "NaN"

themes = [
    "blue",
    "love",
    "cutepie",
    "rose",
    "Sky",
    "pink",
    "rabbit",
    "mastii",
    "cutegirl",
    "cutedoll",
]

def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    theme = random.choice(themes)
    image1 = Image.open("./background.png")
    image2 = Image.open(f"resource/{theme}.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resource/font.otf", 32)
    draw.text((190, 550), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Powered By: Bikash Halder (@BikashHalder)",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["play", "/play", "yt", "ytp", "/yt", "/ytp", "@", "#", "bgt", ".play"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    lel = await message.reply("**🔎 Zoney Ki GF Bhag Gai ...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "𓆩𝐈𝐍𝐃🇮🇳𓆪 ❥ ̶͢ ̶ͨ ̶ͧ ̶ͭ ̶ͤ❤⃝⃝𝐑𝐔𝐂𝐇𝐈𝐓𓆩♡𓆪🥀』"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "**ॐ At ፠ First ☞ Make ༒ Me ᯼ Admin 👑 ...**")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**ॐ I 🐼 αɱ 🌀 Rҽαԃყ 🍫 Tσ 🌺 Pʅαყ 🎼 ...**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"**🐬 Pʅҽαʂҽ ❤️ Mαɳυαʅʅყ 🌺 Aԃԃ 👉 Aʂʂιʂƚαɳƚ 😔 σ𝐫 🎸 Cσɳƚαƈƚ 👑 ƚσ ː [꧁🕊 Ɩ'M⚡Bikคsђ 🕊꧂](https://t.me/BikashHalder) 🌺**")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"**🐬 Pʅҽαʂҽ ❤️ Mαɳυαʅʅყ 🌺 Aԃԃ 👉 Aʂʂιʂƚαɳƚ 😔 σ𝐫 🎸 Cσɳƚαƈƚ 👑 ƚσ ː [꧁🕊 Ɩ'M⚡Bikคsђ 🕊꧂](https://t.me/BikashHalder) 🌺**")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**💥 Pʅαყ 🔊 Mυʂιƈ 💿 Lҽʂʂ ⚡️\n🤟 Tԋαɳ⚡️ {DURATION_LIMIT} 💞 Mιɳυƚҽ ...**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/b559b922fe86fc0ab2285.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴍᴇɴᴜ ✯",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=f"https://t.me/FULL_ON_MOJJ_MASTI"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴍᴇɴᴜ ✯",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=f"https://t.me/FULL_ON_MOJJ_MASTI"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/b559b922fe86fc0ab2285.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
[
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴍᴇɴᴜ ✯",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=f"https://t.me/FULL_ON_MOJJ_MASTI"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
            ),
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 Pʅαყ 🔊 Mυʂιƈ 💿 Lҽʂʂ ⚡️\n🤟 Tԋαɳ⚡️ {DURATION_LIMIT} 💞 Mιɳυƚҽ ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**🤖 Gιʋҽ 🙃 Mυʂιƈ 💿 Nαɱҽ 😍\n💞 Tσ 🔊 Pʅαყ 🥀 Sσɳɠ 🌷...**"
            )
        await lel.edit("**🔄 𝐓𝐡𝐨𝐝𝐚 𝐖𝐚𝐢𝐭 𝐁𝐚𝐛𝐲 🥺 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🔊 Mυʂιƈ 😕 Nσƚ 📵 Fσυɳԃ❗️\n💞 Tɾყ ♨️ Aɳσƚԋҽɾ 🌷...**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
         [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴍᴇɴᴜ ✯",
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=f"https://t.me/FULL_ON_MOJJ_MASTI"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 Pʅαყ 🔊 Mυʂιƈ 💿 Lҽʂʂ ⚡️\n🤟 Tԋαɳ⚡️ {DURATION_LIMIT} 💞 Mιɳυƚҽ ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="**💥 𝑻𝒆𝒂𝒎 𝑰𝒏𝒅 🌷 Mυʂιƈ 💿 Nσɯ❗️\n🔊 Qυҽυҽԃ 🌀 αƚ » `{}` 🌸 ...**".format(position),
            reply_markup=keyboard,
        )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**💥 𝑻𝒆𝒂𝒎 𝑰𝒏𝒅 🌺 Mυʂιƈ 🎸 Nσɯ 💞\n🔊 Pʅαყιɳɠ 😍 σρ 🥀 ...**".format(),
           )

    os.remove("final.png")
    return await lel.delete()
    
    
@Client.on_message(commandpro([".pause", "/pause", "pause", ".pse"]) & other_filters)
@errors
#@authorized_users_only
async def pause(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("**▶️ Pαυʂҽԃ 🌺 ...**"
    )


@Client.on_message(commandpro([".resume", "/resume", "resume", ".rsm"]) & other_filters)
@errors
#@authorized_users_only
async def resume(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("**⏸ Rҽʂυɱҽԃ 🚫 ...**"
    )



@Client.on_message(commandpro([".skip", "skip", "/skip", ".skp"]) & other_filters)
@errors
#@authorized_users_only
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**Baby tum bohot Gande ho 🥺... ...**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            await message.reply_text("*Baby tum bohot Gande ho 🥺...**") 
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )



@Client.on_message(commandpro([".end", "/end", "end", "x", ".stp"]) & other_filters)
@errors
#@authorized_users_only
async def stop(_, message: Message):
    await message.delete()
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("**Baby tum bohot Gande ho 🥺...**"
    )


@Client.on_message(commandpro([".reload", ".refresh", ".rld", "/reload", "reload"]))
@errors
@authorized_users_only
async def update_admin(client, message):
    global a
    await message.delete()
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    a[message.chat.id] = new_admins
    await message.reply_text(
        "**🔁 R𝐞L𝐨a𝐝e𝐝 ♻ ...**"
    )
