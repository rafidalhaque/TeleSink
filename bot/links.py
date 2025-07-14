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
site = os.getenv("SITE")
site_token = os.getenv("SITE_TOKEN")
api_url = f"{site}/api/link/create"
headers = {
    "Authorization": f"Bearer {site_token}",
    "Content-Type": "application/json"
}

# slug generation
def generate_slug(length=5):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

# start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Assalamu Alaikum!")

async def link_shorten(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args

    if len(args) == 1:
        await update.message.reply_text("Format:\n/shorten <link> <slug>\n\n_if you don't give the slug, slug will be automatically generated.")

    link = args[0]
    slug = args[1] if len(args) > 1 else generate_slug()
    payload = {
        "link": link,
        "slug": slug
    }

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()