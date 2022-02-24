from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')

bot = Client('droplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}! Welcome To my world 😈**\n\n"
        "**🤖 Iam Tnvalue converter bot\n 🔄 I am a best Tnvalue bot\n🧑‍💻 I was developed @half_intelligent_2 \n ✅For accuses ask @half_intelligent_2 \n 😅Use me & enjoy **")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f' your Shorted Tnvalue ➢ [`{short_link}`]({short_link})', quote=True)

    except Exception as e:

        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://link.tnvalue.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
