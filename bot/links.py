# packages
import json
import string
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from dotenv import load_dotenv
import os
import aiohttp
from pathlib import Path
import logging

# load .env file from root/env/.env
env_path = Path('..') / 'env' / '.env'
load_dotenv(dotenv_path=env_path)

# load variables from .env
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
site = os.getenv("SITE")
site_token = os.getenv("SITE_TOKEN")
api_url = f"{site}/api/link/create"
headers = {
    "Authorization": f"Bearer {site_token}",
    "Content-Type": "application/json"
}

# enable logging for easy debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Use DEBUG for maximum verbosity
)

# ---------------- message text ------------------------------
start = """🌀 Welcome to TeleSink!

I’m your quick-link ninja 🥷 — I shorten links for you using the Sinks API.

Try:
  /shorten https://example.com myslug

or let me pick a slug for you:
  /shorten https://example.com

Need help? Hit /help

"""

help = """📖 *TeleSink Bot Help*

I shorten long URLs into slick, short ones.

🔧 *Commands:*
• `/start` — Greet the bot
• `/shorten <link> <slug?>` — Create a shortened URL
   ⤷ Slug is optional; I’ll generate one if you skip it
• `/help` — Show this help message

🔗 *Example:*
  /shorten https://example.com/docs mydoc

Result:
  ✅ https://sub.domain.tld/mydoc

💻 *Source Code*

[GitHub Repo](https://github.com/rafidalhaque/TeleSink) | [GitHub Repo of Sink](https://github.com/ccbikai/Sink)

—
Built with 💖 by @CosmopoliteMuslim & ChatGPT 😎

"""
# ---------------- start bot --------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Assalamu Alaikum!")

# ----------------  link shortener using links.teamsabily.tech  ------------------------------
# slug generation
def generate_slug(length=5):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

# link shortening
async def link_shorten(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args

    if len(args) == 1:
        await update.message.reply_text("Format:\n```\n/shorten <link> <slug>\n```\n_if you don't give the slug, slug will be automatically generated._", parse_mode='Markdown')

    link = args[0]
    slug = args[1] if len(args) > 1 else generate_slug()
    payload = {
        "url": link,
        "slug": slug
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, headers=headers, json=payload) as response:
                if response.status == 201:
                    res = await response.json()
                    await update.message.reply_text(f"✅ Shortened Link: {site}/{slug}. \n\n\n\nResponse as JSON:```\n{json.dumps(res, indent=2)}\n```", parse_mode='Markdown')
                # elif response.status == 409:
                #     slug = generate_slug()
                else:
                    error_text = await response.text()
                    await update.message.reply_text(f"**❌ API Error**\nError {response.status}:{error_text}\n\n**Payload:**\n```\n{json.dumps(payload, indent=2)}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"🚨 Request failed:\n{e}")
# ------------------ help function -------------------------
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(help, parse_mode='Markdown')

# ------------------  main function -------------------------
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shorten", link_shorten))
    app.add_handler(CommandHandler("help", help))
    app.run_polling()