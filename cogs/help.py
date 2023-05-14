import disnake
from disnake.ext import commands
import config

class Help(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Показывает все команды сервера")
    async def help(self , ctx):
        embed = disnake.Embed(
            color=0xffffff,
            description=config.data['help']
        )
        await ctx.send(embed=embed , ephemeral=True)


def setup(bot):
    bot.add_cog(Help(bot))