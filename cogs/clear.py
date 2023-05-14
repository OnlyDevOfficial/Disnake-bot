import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Clear(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Эта команда удаляет сообщения в чате")
    @commands.has_permissions(administrator=True)
    async def clear(self , ctx , amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Удалено {amount} сообщений")


def setup(bot):
    bot.add_cog(Clear(bot))