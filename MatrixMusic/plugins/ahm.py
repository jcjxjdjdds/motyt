from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from AnonX import app

hmses = {}

@app.on_message(filters.reply & filters.regex("همسه") & filters.group)
async def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(await app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("- اضغط لإرسال الهمسه!", url=start_link)]
        ]
    )
    await message.reply_text("\n╢ إضغط لإرسال همسه!\n", reply_markup=reply_markup, reply_to_message_id=message.message_id)

waiting_for_hms = False
@app.on_message(filters.command("start"), group=473)
async def hms_start(client, message):
  if message.text.split(" ", 1)[-1].startswith("hms"):
    global waiting_for_hms, hms_ids
    hms_ids = message.text
    waiting_for_hms = True
    await message.reply_text(
      "-> أرسل الهمسه الآن.\n√",
      reply_markup = InlineKeyboardMarkup ([[
        InlineKeyboardButton ("إلغاء ❌️", callback_data="hms_cancel")
      ]])
    )
    return

@app.on_message(filters.private & filters.text & ~filters.command("start"), group=921)
async def send_hms(client, message):
  global waiting_for_hms
  if waiting_for_hms:    
    to_id = int(hms_ids.split("to")[-1].split("in")[0])
    from_id = int(hms_ids.split("hms")[-1].split("to")[0])
    in_id = int(hms_ids.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    
    hmses[str(to_id)] = { "hms" : message.text, "bar" : in_id }
    
    await message.reply_text("-> تم ارسال الهمسه.\n√")
    
    await app.send_message(
      chat_id = in_id,
      text = f"╖ المستخدم [{(await app.get_chat(to_id)).first_name}]({to_url})\n╢ لديك همسه من البني آدم دا [{(await app.get_chat(from_id)).first_name}]({from_url})\n╜انت فقط من يستطيع رؤيتها 🔐",
      reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton("- اضغط لرؤية الهمسه 👀", callback_data = "hms_answer")]])
    )
    
    waiting_for_hms = False
  
@app.on_callback_query(filters.regex("hms_answer"))
async def display_hms(client, callback):
  in_id = callback.message.chat.id
  who_id = callback.from_user.id
  
  if hmses.get(str(who_id)) is not None:
    if hmses.get(str(who_id))["bar"] == in_id:
      await callback.answer( hmses.get(str(who_id))["hms"], show_alert = True )
  else:
    await callback.answer( "بطل لعب ف حاجه مش بتاعتك يابابا 🗿", show_alert = True )
    
@app.on_callback_query(filters.regex("hms_cancel"))
async def cancel_hms(client, callback):
  
  global waiting_for_hms
  waiting_for_hms = False
  
  await client.edit_message_text(
      chat_id = callback.message.chat.id,
      message_id = callback.message.id,
      text = "-> تم إلغاء الهمسه!\n√")
  
