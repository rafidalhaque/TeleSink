import string
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

env_path = Path('..') / 'env' / '.env'
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("TG_BOT_TOKEN")

# start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Assalamu Alaikum!")


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()