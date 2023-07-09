$ docker pull ghcr.io/channel-mirrors/conda-forge/noarch/discord.py:2.2.3-pyhd8ed1ab_0
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, '+ str(message.author))
    else:
        await message.channel.send('idk what that was bruh what did you say')

client.run(secret.TOKEN)
