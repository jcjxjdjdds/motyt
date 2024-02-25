import requests
import json
from MatrixMusic import app
from pyrogram import Client
from pyrogram import filters
from os import system
try: from pyrogram import Client, filters
except ImportError:
    system('pip install pyrogram tgcrypto')
    from pyrogram import Client, filters
from pyrogram.types import Message
try: import requests
except ImportError:
    system('pip install requests')
    import requests



api = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(query):
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':query,
        }
    }

    response = requests.post(api, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return None


@app.on_message(filters.command('مارو', ''))
async def gpt_reply(client, message):
    wait = await message.reply_text("↯︙تم استلام سؤال لـ ↫ ⦗ سيرفرات هيروكو ⦘", reply_to_message_id = message.id)
    data = message.text.split(maxsplit=1)
    if len(data) == 1: return await wait.edit_text('يرجى تحديد سؤال')
    ai_answer = gpt(data[1])
    return await wait.edit_text(ai_answer if ai_answer else 'عذرا عزيزي تعذر الرد !')
