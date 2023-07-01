import disnake
from disnake.ext import commands
from db import DataBase
import config
import random

class Kiss(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Хочешь кого нибудь поцеловать?")
    async def kiss(self , ctx , member: disnake.Member):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            gif = random.choice(config.data["kiss"])
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Поцелуй",
                description=f"{ctx.author.mention} целует {member.mention}"
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
    bot.add_cog(Kiss(bot))