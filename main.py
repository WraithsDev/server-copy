mytitle = "WraithsDev-Server-Copy"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}<

 __          __        _ _   _         _____             
 \ \        / /       (_) | | |       |  __ \            
  \ \  /\  / / __ __ _ _| |_| |__  ___| |  | | _____   __
   \ \/  \/ / '__/ _` | | __| '_ \/ __| |  | |/ _ \ \ / /
    \  /\  /| | | (_| | | |_| | | \__ \ |__| |  __/\ V / 
     \/  \/ |_|  \__,_|_|\__|_| |_|___/_____/ \___| \_/  

                   WraithsDev-Server-Copy
{Style.RESET_ALL}
        """)
token = input(f'Token:\n >')
guild_s = input('Aktarılan Sunucu ID:\n >')
guild = input('Aktarım Sağlanan Sunucu ID:\n >')
input_guild_id = guild_s
output_guild_id = guild
token = token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Olarak giriş yaptı : {client.user}")
    print("Aktarım Başladı...")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
          Aktarım Tamamlandı...
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()

client.run(token, bot=False)
