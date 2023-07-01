import disnake
from disnake.ext import commands
from db import DataBase
import config
import random

class Food(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Едаааа")
    async def food(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            image = random.choice(config.data['food'])
            embed = disnake.Embed(
                color=disnake.Color.green()
            )
            embed.set_image(image)

            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Food(bot))