from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Avatar(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Показывает аватарку пользователя")
    async def avatar(self , ctx , member: disnake.Member = None):
        user = member or ctx.author
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title=f"Аватар __{ctx.author.name}__"
        )
        embed.set_image(user.display_avatar.url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Avatar(bot))