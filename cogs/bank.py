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
        user_name , money , level , bank , work = self.DataBase.data(ctx.author.id)
        if money >= bet:
            if bank + bet > 5000000:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Банк заполнен",
                    description=f"В банке можно хранить не больше 2000000🍬"
                )

                await ctx.send(embed=embed)
            
            else:

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