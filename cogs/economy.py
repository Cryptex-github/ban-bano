import discord
from discord.ext import commands
from utils.asyncstuff import asyncexe
import json

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @asyncexe()
    def open_(self, author):
        with open("bank.json", "r") as f:
            users = json.load(f)
            if str(author.id) in users:
                return True
            else:
                users[str(author.id)]["wallet"] = 0
                users[str(author.id)]["bank"] = 0
                with open("bank.json", "w") as f:
                    json.dump(users, f)

    @asyncexe()
    def bal_(self, author):
        with open("bank.json", "r") as f:
            users = json.load(f)
            if str(author.id) in users:
                return users[str(author.id)]["wallet"], users[str(author.id)]["bank"]
            else:
                return False

    @commands.command()
    async def bal(self, ctx, user:discord.Member=None):
        wallet, bank = await self.bal_(user or ctx.author)
        await ctx.send(embed=discord.Embed(description=f"Wallet: {wallet}\nBank: {bank}"))

    @commands.command()
    async def open(self, ctx):
        await self.open_(ctx.author)
        await ctx.send(f"Succefully opened bank account {ctx.author.id}")
    





def setup(bot):
    bot.add_cog(economy(bot))