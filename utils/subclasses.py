import discord
from discord.ext import commands

class BanBanoContext(commands.Context):
    pass

class BanBano(commands.Bot):
    async def get_context(self, message, *, cls=BanBanoContext):
        return await super().get_context(message, cls=cls)