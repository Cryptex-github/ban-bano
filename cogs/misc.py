import discord
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mouse(self, ctx):
        await ctx.send("is fat")

def setup(bot):
    bot.add_cog(misc(bot))