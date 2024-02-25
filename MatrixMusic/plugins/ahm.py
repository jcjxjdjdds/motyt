from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup

matrixes = {}
@app.on_message(filters.reply & filters.regex("اهمس") & filters.group)
def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(matrixpyrogram.get_me()).username}?start=matrix{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("‹ اضغط هنا ›", url=start_link)]
        ]
    )
    message.reply_text("↯︙اضـغط هنا ↫ ⦗ لإرسال الهمسة السرية ⦘", reply_markup=reply_markup)
waiting_for_matrix = False
@app.on_message(filters.command("start"))
def matrix_start(client, message):
  
  if message.text.split(" ", 1)[-1].startswith("matrix"):
    global waiting_for_matrix, matrix_ids
    matrix_ids = message.text
    waiting_for_matrix = True
    message.reply_text(
      "↯︙ارسل رسالتك",
      reply_markup = InlineKeyboardMarkup ([[
        InlineKeyboardButton ("‹ إلغاء ›", callback_data="matrix_cancel")
      ]])
    )
    return
@app.on_message(filters.private & filters.text & ~filters.command("start"))
def send_matrix(client, message):
  
  global waiting_for_matrix
  if waiting_for_matrix:    
    to_id = int(matrix_ids.split("to")[-1].split("in")[0])
    from_id = int(matrix_ids.split("matrix")[-1].split("to")[0])
    in_id = int(matrix_ids.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    
    matrixes[str(to_id)] = { "matrix" : message.text, "bar" : in_id }
    
    message.reply_text("↯︙تم إرسال الهمسة")
    
    matrixpyrogram.send_message(
      chat_id = in_id,
      text = f"↯︙هذي الهمسة للحلو ↬ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\n↯︙هو اللي يقدر يشوفها ↬ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘",
      reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton("‹ لرؤية الهمسة ›", callback_data = "matrix_answer")]])
    )
    
    waiting_for_matrix = False
  
@matrixpyrogram.on_callback_query(filters.regex("matrix_answer"))
def display_matrix(client, callback):
  
  in_id = callback.message.chat.id
  who_id = callback.from_user.id
  
  if matrixes.get(str(who_id)) is not None:
    if matrixes.get(str(who_id))["bar"] == in_id:
      callback.answer( matrixes.get(str(who_id))["matrix"], show_alert = True )
  else:
    callback.answer( "هذا الأمر لايخصك", show_alert = True )
    
@app.on_callback_query(filters.regex("matrix_cancel"))
def cancel_matrix(client, callback):
  
  global waiting_for_matrix
  waiting_for_matrix = False
  
  matrixpyrogram.edit_message_text(
  chat_id = callback.message.chat.id,
  message_id = callback.message.id,
  text = "↯︙تم الغاء ↫ ⦗ الهمسة ⦘")
