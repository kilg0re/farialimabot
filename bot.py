import os
import random
import discord
from dotenv import load_dotenv

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
    if "!flip a coin" in message_content:
        result = {0: 'heads', 1: 'tails'}[random.randint(0, 1)]
        await message.channel.send(result)

client.run(token)
