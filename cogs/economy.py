import discord
from discord.ext import commands
from utils.asyncstuff import asyncexe
import json

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @asyncexe()
    def confirm(self, author):
        with open("bank.json", "r") as f:
            users = json.load(f)
            if str(author.id) in users:
                return True
            else:
                return False
    @asyncexe()
    def open_(self, author):
        with open("bank.json", "r") as f:
            users = json.load(f)
            if str(author.id) in users:
                return True
            else:
                users[str(author.id)] = {}
                users[str(author.id)]["wallet"] = 0
                users[str(author.id)]["bank"] = 0
                with open("bank.json", "w") as f:
                    json.dump(users, f, indent=4)

    @asyncexe()
    def change_(self, author, type_:str="wallet", amount:int=0):
        with open("bank.json", "r") as f:
            users = json.load(f)
            bal = users[str(author.id)][type_]
            bal += amount
            users[str(author.id)][type_] = bal
            with open("bank.json", "w") as f:
                json.dump(users, f, indent=4)
                return True





    @asyncexe()
    def bal_(self, author):
        with open("bank.json", "r") as f:
            users = json.load(f)
            if str(author.id) in users:
                return users[str(author.id)]["wallet"], users[str(author.id)]["bank"]
            else:
                return None, None

    @commands.command()
    async def bal(self, ctx, user:discord.Member=None):
        wallet, bank = await self.bal_(user or ctx.author)
        if bank == None:
            return await ctx.send("u don't even have a bank account run `open` to open one")
        await ctx.send(embed=discord.Embed(description=f"Wallet: {wallet}\nBank: {bank}"))

    @commands.command()
    async def open(self, ctx):
        o = await self.open_(ctx.author)
        if o:
            return await ctx.send("you already have a bank account")
        await ctx.send(f"Succefully opened bank account {ctx.author.id}")
    
    @commands.command()
    async def change(self, ctx, user:discord.Member, amount):
        if not await self.confirm(user):
            return await ctx.send(f"{user} don't have a account")
        await self.change_(user, "wallet", amount)
        wallet, bank = await self.bal_(user)
        return await ctx.send(f"Success, the user's balance is now \n wallet: {wallet}\n bank: {bank}")
    





def setup(bot):
    bot.add_cog(economy(bot))