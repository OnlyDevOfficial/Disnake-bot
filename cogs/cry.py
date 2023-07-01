import disnake
from disnake.ext import commands
import config
from db import DataBase
import datetime
import random

class Cry(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Поплачь еще")
    async def cry(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            gif = random.choice(config.data["cry"])
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Плач",
                description=f"{ctx.author.mention} плачет"
            )
            date = datetime.datetime.now()
            embed.set_footer(text=f"{date}")
            embed.set_image(gif)

            await ctx.send(embed=embed)

        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cry(bot))