from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Take(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Снимай деньги с банка оккуратно!")
    async def take(self , ctx , bet: int):
        user_name , money , level , bank , work = self.DataBase.data(ctx.author.id)
        if bank >= bet:
            self.DataBase.take(ctx.author.id , bet)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Снятие с банка",
                description=f"Вы успешно сняли с карты {bet}🍬"
            )

            await ctx.send(embed=embed)

        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Недостаточно средств",
                description=f"На вашей карте недостаточно средств!"
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Take(bot))