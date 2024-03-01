import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import app
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    command(["المطور","مطوره","تونز","مطور السورس","مبرمج السورس"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("AL_G_A_D_A_R_A2")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["مارش"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("Marshmello_x_x")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["مطورين","مطورين السورس","المطورين","سورس","السورس"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7a4ea9510adbff3564608.jpg",
        caption=f"""↯︙اهلا بك عزيزي {message.from_user.mention}\n↯︙مطورين سورس دارك ميوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ : 𝗗𝗘𝗩 𝐷𝐴𝑅𝐾 : ›", url=f"https://t.me/T4_Mohamed"), 
                 ],[
                    InlineKeyboardButton(
                        "‹ :مـًٌٍّ̨̥̬̩ـمـ༈ۖ҉ـآرٍشـًٌٍّ̨̥̬̩ـمـًٌٍّ̨̥̬̩ـيلُـِـِِـِِِؤ❾ فـ༈ۖ҉ـء : ›", url=f"https://t.me/Marshmello_x_x"),
                ],[
                    InlineKeyboardButton(
                        "‹ : 𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 : ›", url=f"https://t.me/S_MA4"),
                ],

            ]

        ),

    )

@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 : ›", url=f"https://t.me/S_MA4"),
           ],
       ]
    ),
