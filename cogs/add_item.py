from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Add_item(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Добавить предмет в магазин")
    @commands.has_permissions(administrator=True)
    async def add_item(self , ctx , name: str , price: int , role: str):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            self.DataBase.add_item(name , price , role , ctx.author.guild.name)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Новый предмет",
                description=f"Предмет {name} был успешно добавлен в магазин"
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
    bot.add_cog(Add_item(bot))