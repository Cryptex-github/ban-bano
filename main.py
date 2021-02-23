import discord
from discord.ext import commands
from utils.subclasses import BanBano
import os
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = BanBano(command_prefix=".", intents=intents)

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(TOKEN)