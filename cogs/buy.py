from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Buy(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Не хочешь чего нибудь купить?")
    async def buy(self , ctx , name):
        result = self.DataBase.buy(name , ctx.author.id)
        if result == "На вашем счету недостаточно средств!":
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Недостаточно средств",
                description=result
            )

            await ctx.send(embed=embed)

        else:
            guild = self.bot.get_guild(ctx.guild.id)
            role = guild.get_role(result)
            
            await ctx.author.add_roles(role)

            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Покупка",
                description=f"Поздравляю! Вы приобрели роль {role}"
            )

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Buy(bot))