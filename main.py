import discord
from discord.ext import commands
from utils.subclasses import BanBano
import os
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = BanBano(command_prefix=".", intents=intents)

bot.run(TOKEN)