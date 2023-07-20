import discord
from discord import app_commands
import os
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


test = []
"""@tree.command(name = "add", description = "add something to memory")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")"""


@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} online')
@slash.slash(name="fact", description="Get a random fact")
async def get_fact(ctx: SlashContext):
    fact = get_random_fact()
    embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
    await ctx.send(embed=embed, components=[create_button()])

@client.event
async def on_component(ctx):
    if ctx.component_id == "get_fact":
        fact = get_random_fact()
        embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
        await ctx.edit_origin(embed=embed, components=[create_button()])

def get_random_fact():
    with open('facts.txt', 'r') as file:
        facts = file.readlines()
        fact = "a"
    return fact

def create_button():
    return [
        {
            "type": 1,
            "components": [
                {
                    "type": 2,
                    "label": "Get another fact",
                    "style": 1,
                    "custom_id": "get_fact"
                }
            ]
        }
    ]
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, @'+ str(message.author))
    else:
        await message.channel.send('idk what that was bruh what did you say')

client.run(str(os.getenv("TOKEN")))
