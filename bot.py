import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
TOKEN=os.getenv("BOT_TOKEN")
ISLAMIC=[("خالد الحيالي","https://t.me/GPS6100/101"),("ساجد العكيلي","https://t.me/GPS6100/102"),("عدنان","https://t.me/GPS6100/103"),("محمد الجنابي","https://t.me/GPS6100/104"),("هشام المعموري","https://t.me/GPS6100/105"),("عمار فاضل","https://t.me/GPS6100/106")]
ARABIC=[("عقيل الزبيدي","https://t.me/GPS6100/201"),("حمزة الجابري","https://t.me/GPS6100/202"),("احمد النعيمي","https://t.me/GPS6100/203"),("حسين عبيس","https://t.me/GPS6100/204"),("حيدر جلوخان","https://t.me/GPS6100/205")]
async def start(update,context):
 kb=[[InlineKeyboardButton("علمي",callback_data="ilmi"),InlineKeyboardButton("ادبي",callback_data="adabi")]]
 await update.message.reply_text("بوت ملازم @GPS6100\nاختر فرعك:",reply_markup=InlineKeyboardMarkup(kb))
async def btn(update,context):
 q=update.callback_query;await q.answer();d=q.data
 if d in ["ilmi","adabi"]:
  context.user_data["b"]=d;kb=[[InlineKeyboardButton("اسلامية (6)",callback_data="isl"),InlineKeyboardButton("عربي (37)",callback_data="arb")]]
  await q.edit_message_text("اختر المادة:",reply_markup=InlineKeyboardMarkup(kb))
 elif d=="isl":
  kb=[[InlineKeyboardButton(n,url=l)] for n,l in ISLAMIC];kb.append([InlineKeyboardButton("رجوع",callback_data=context.user_data.get("b","ilmi"))])
  await q.edit_message_text("ملازم الاسلامية:",reply_markup=InlineKeyboardMarkup(kb))
 elif d=="arb":
  kb=[[InlineKeyboardButton(n,url=l)] for n,l in ARABIC];kb.append([InlineKeyboardButton("رجوع",callback_data=context.user_data.get("b","ilmi"))])
  await q.edit_message_text("ملازم العربي:",reply_markup=InlineKeyboardMarkup(kb))
def main():
 app=Application.builder().token(TOKEN).build();app.add_handler(CommandHandler("start",start));app.add_handler(CallbackQueryHandler(btn));app.run_polling()
if __name__=="__main__":main()
