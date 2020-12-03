from telethon import TelegramClient
API_KEY = "1597604"
API_HASH = "afa675e093d83bd9023b00f766f69caf"
# get it from my.telegram.org
bot = TelegramClient('userbot', API_KEY, API_HASH)
bot.start()

# This script wont run your bot, it just generates a session.
