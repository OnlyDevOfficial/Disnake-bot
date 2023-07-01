from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Avatar(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Показывает аватарку пользователя")
    async def avatar(self , ctx , member: disnake.Member):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            user = member or ctx.author
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title=f"Аватар __{member.name}__"
            )
            date = datetime.datetime.now()
            embed.set_footer(text=f"{date}")
            embed.set_image(user.display_avatar.url)
            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Avatar(bot))