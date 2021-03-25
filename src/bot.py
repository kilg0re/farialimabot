import random
import os
import discord
from dotenv import load_dotenv

import api

# get bot and guild tokens from environment
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
my_guild = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

@client.event
async def on_message(message):
    message_content = message.content.lower()
    if "!quote" in message_content:
        symbol = message_content.split(' ')[1]
        print(symbol)
        quote = api.quote_stock(symbol.upper())
        await message.channel.send(quote)

client.run(token)
