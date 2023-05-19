from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Bank(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Преводи деньги в банк пока их не украли!")
    async def bank(self , ctx , bet: int):
        user_name , money , level , bank = self.DataBase.data(ctx.author.id)
        if money >= bet:
            self.DataBase.bank(ctx.author.id , bet)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Перевод в банк",
                description=f"Вы успешно перевели в банк {bet}🍬"
            )

            await ctx.send(embed=embed)

        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Недостаточно средств",
                description=f"На вашем счету недостаточно средств!"
            )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Bank(bot))