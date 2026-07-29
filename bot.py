from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "
8581805593:AAFhjjFKzq0Lah5nYx4tO3Ud8LOn5GdD3Ww"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! HackBot is running.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()