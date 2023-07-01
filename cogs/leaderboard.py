from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random 

class LeaderBoard(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Топы сервера")
    async def leaderboard(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Leaderboard"
            )
            embed.set_thumbnail(ctx.author.display_avatar.url)
            result = self.DataBase.leaderboard(ctx.author.guild.name)
            result = sorted(result , key=lambda top: top[4] + top[3] , reverse=True)
            number = 0
            for i in result:
                if number != 5:
                    number = number + 1
                    embed.add_field(
                        name=i[2],
                        value=f"""
                        Bank: {i[3]}
                        Money: {i[4]}
                        """,
                        inline=False
                    )

            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(LeaderBoard(bot))