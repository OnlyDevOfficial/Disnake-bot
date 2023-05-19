from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Work(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Пахай негр")
    @commands.cooldown(1, 60*60*12 , commands.BucketType.user)
    async def work(self , ctx):
        win = random.randint(3000 , 10000)
        # add_time = None
        self.DataBase.work(win , ctx.author.id)
        # self.DataBase.add_time_work(ctx.author.id , )
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Работа",
            description=f"Пользователь __{ctx.author.name}__ заработал {win}🍬"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Work(bot))