# 🚀 TeleSink — Telegram Link Shortener Bot

**TeleSink** is a blazing-fast, Telegram-based URL shortener powered by the [Sink](https://github.com/ccbikai/Sink) API.

Shrink your long, ugly links into clean short URLs — directly from Telegram. ⚡️
Just send `/shorten <link> <optional-slug>` and let the bot handle the rest.

---

## ✨ Features

* 🔗 **Instant Link Shortening** via `/shorten`
* 🤖 **Simple, Clean Bot Interface**
* 🧠 **Auto Slug Generation** if none provided
* 📦 **Integrated with Sink API**
* 🌐 **Deployable with .env configuration**
* ✅ Built with [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)

---

## ⚙️ Commands

| Command                 | Description                         |
|-------------------------| ----------------------------------- |
| `/start`                | Say hello to the bot                |
| `/shorten <url> <slug?>` | Shorten any link with optional slug |
| `/help`                 | Show help instructions              |

Example:

```text
/shorten https://example.com/some/long/path myslug
```

Result:

```
✅ Shortened Link:
https://sub.domain.tld/myslug
```

---

## 🛠️ Environment Variables

Create an `.env` file inside an `env/` folder Or, Copy the `.env.sample` to `.env`:

```env
TG_BOT_TOKEN=your_telegram_bot_token
SITE=https://sub.domain.tld
SITE_TOKEN=your_sink_site_token
```
---

## 📦 Requirements

* Python 3.10+
* Dependencies:

  ```bash
  pip install python-telegram-bot aiohttp python-dotenv
  ```

---

## 🚀 Run It

```bash
python links.py
```

✅ Done. Now go test your bot on Telegram.

---

## 📄 License

MIT — Free to modify, use, and distribute.

---

## 🙌 Credits

* 🔗 [Sinks API](https://github.com/ccbikai/Sink)
* 🤖 [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* ✨ Developed with ❤️ by [@CosmopoliteMuslim](https://t.me/CosmopoliteMuslim)

---
