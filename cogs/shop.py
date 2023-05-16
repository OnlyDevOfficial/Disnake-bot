from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Shop(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Магазинчик)")
    async def shop(self , ctx):
        result = self.DataBase.shop()
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Магазин",
        )
        for i in result:
            name = str(i[0])
            price = i[1]
            role = i[0]
            embed.add_field(
                name=name,
                value=f"\nPrice: {price}\nRole: {role}",
                inline=False
            )
            
        await ctx.send(embed=embed)
    


def setup(bot):
    bot.add_cog(Shop(bot))