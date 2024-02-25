import asyncio
from pyrogram import Client, filters ,enums
from strings.filters import command
from pyrogram.types import *
from MatrixMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ParseMode, ChatMemberStatus

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}AHMEDRD")[1].replace("\n",""))
    return False

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}AHMEDRD{rd}\n")
    return True

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return


'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "- قائمة المشرفين\n— — — — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f"› {'@'+admins.user.username if admins.user.username else admins.user.mention} - `{admins.user.id}` .\n"
    await message.reply(text=(admin))

@app.on_message(filters.regex("^البوتات$"))
async def botslist(_, message):
    chat_id = message.chat.id
    rnryr = "- قائمة البوتات\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
           rnryr+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(ahmed))
'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
@app.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(client, message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    MATRIXAR1 = await app.MATRIXAR(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = MATRIXAR1.text
    MATRIXAR2 = await app.MATRIXAR(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=MATRIXAR1.id, filters=filters.user(message.from_user.id))
    copy = await MATRIXAR2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await MATRIXAR2.reply("تم اضافة الرد بنجاح")
    else: return await MATRIXAR2.reply("حدث خطأ")

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
@app.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(client, message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   MATRIXAR = await app.MATRIXAR(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(MATRIXAR.text, message.chat.id)
   if not a:
     return await MATRIXAR.reply("الرد غير موجود")
   x = f"{message.chat.id}#{MATRIXAR.text}AHMEDRD{a}"
   b = del_rd(x)
   await MATRIXAR.reply("• تم مسح الرد")
   

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
@app.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(client, message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
@app.on_message(filters.regex("افتاره"))
async def her(_, message):
     user_id = message.reply_to_message.from_user.id
     d = await app.get_chat(user_id)
     photo = await app.download_media(d.photo.big_file_id)
     bio = d.bio
     if photo:
        await message.reply_photo(photo,caption=bio)
     else:
        await message.reply(bio)
        
@app.on_message(filters.regex("افتاري"))
async def my(_, message):
     user_id = message.from_user.id
     b = await app.get_chat(user_id)
     photo = await app.download_media(b.photo.big_file_id)
     bio = b.bio
     if photo:
        await message.reply_photo(photo,caption=bio)
     else:
        await message.reply(bio)

@app.on_message(filters.regex("^بايو$"))
async def Bio(_, message):
    if not message.reply_to_message:
     me = message.from_user.id
     b = await app.get_chat(me)
     bio = b.bio
     await message.reply_text(bio)
	
@app.on_message(filters.regex("^بايو$"))
async def Bio(_, message):
	if message.reply_to_message:
		user_id = message.reply_to_message.from_user.id
		d = await app.get_chat(user_id)
		bio = d.bio
		await message.reply_text(bio)

@app.on_message(filters.regex("قول"))
async def echo(_, msg):
 text = msg.text.split(None, 1)[1]
 await msg.reply(text)

'''
Programmed by : 🎖️ @RNRYR
   Channel -› • @Matrixthon
'''
