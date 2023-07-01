import disnake
from disnake.ext import commands
import config
from db import DataBase
import random

class Laughter(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Смейся, смейся")
    async def laughter(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            gif = random.choice(config.data["laughter"])
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Смех",
                description=f"{ctx.author.mention} смеется"
            )
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
    bot.add_cog(Laughter(bot))