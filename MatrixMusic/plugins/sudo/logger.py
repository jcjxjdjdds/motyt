from MatrixMusic.plugins.play.filters import command
from pyrogram import filters

from MatrixMusic import app
from MatrixMusic.misc import SUDOERS
from MatrixMusic.utils.database import add_off, add_on
from MatrixMusic.utils.decorators.language import language


@app.on_message(command(["السجل"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "تفعيل":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "تعطيل":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
