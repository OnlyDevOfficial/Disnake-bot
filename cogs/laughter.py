import disnake
from disnake.ext import commands
import config
import random

class Laughter(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Хочешь кого нибудь поцеловать?")
    async def laughter(self , ctx):
        gif = random.choice(config.data["laughter"])
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Смех",
            description=f"{ctx.author.mention} смеется"
        )
        embed.set_image(gif)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Laughter(bot))