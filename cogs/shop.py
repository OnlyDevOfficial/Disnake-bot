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
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            result = self.DataBase.shop(ctx.author.guild.name)
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
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")
                
            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)
    


def setup(bot):
    bot.add_cog(Shop(bot))