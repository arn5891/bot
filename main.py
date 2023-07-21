import discord
from discord import app_commands
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

test = []
@tree.command(name = "add", description = "add 'a' to memory")
async def first(interaction):
    test.append("a")

@tree.command(name = "print", description = "print memory")
async def sec(interaction):
    await interaction.response.send_message(test)

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, @'+ str(message.author))
    else:
        await message.channel.send('idk what that was bruh what did you say')

client.run(str(os.getenv("TOKEN")))
