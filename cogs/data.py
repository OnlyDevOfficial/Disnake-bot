import disnake
import config
from disnake.ext import commands
from db import DataBase

class Data(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')

    @commands.slash_command(description="Показывает ваш профиль")
    async def profile(self , ctx):
        username , balance = self.DataBase.data(ctx.author.id)
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title=f"__Информация о пользователе {username}__",
            description=f"""
Имя: {username}

Ваш счет: {balance}🍬
Уровень: `В разработке`

Присоединился: {ctx.author.joined_at}
            """
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Data(bot))