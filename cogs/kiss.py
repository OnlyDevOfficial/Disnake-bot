import disnake
from disnake.ext import commands
import config
import random

class Kiss(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Хочешь кого нибудь поцеловать?")
    async def kiss(self , ctx , member: disnake.Member):
        gif = random.choice(config.data["kiss"])
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Поцелуй",
            description=f"{ctx.author.mention} целует {member.mention}"
        )
        embed.set_image(gif)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Kiss(bot))