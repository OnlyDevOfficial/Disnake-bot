import disnake
from disnake.ext import commands
import config
import random

class Cry(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Поплачь еще")
    async def cry(self , ctx):
        gif = random.choice(config.data["cry"])
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Плач",
            description=f"{ctx.author.mention} плачет"
        )
        embed.set_image(gif)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cry(bot))