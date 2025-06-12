import datetime
from discord.ext import commands
import discord
from dataclasses import dataclass
import os


BOT_TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1382481249234587738


@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()


@bot.event
async def on_ready():
    print("CraaazyBot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("CraaazyBot is ready!")


@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")




@bot.command()
async def start(ctx, *arr):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
   
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f"New session started at {human_readable_time}")




@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return


    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    await ctx.send(f"Session ended after {human_readable_duration}.")




@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓 ")

    
    
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")





bot.run(BOT_TOKEN)
