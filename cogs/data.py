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
        if self.DataBase.check_user(ctx.author.id) == True:
            username , balance , level , bank , work = self.DataBase.data(ctx.author.id)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title=f"__Информация о пользователе {username}__",
                description=f"""
    Имя: {username}

    Работа: {work}
    Банк: {bank}🍬
    Ваш счет: {balance}🍬
    Уровень: {level}

    Присоединился: {ctx.author.joined_at}
                """
            )

            await ctx.send(embed=embed)

        else:
            self.DataBase.create(ctx.author.id , ctx.author.name)
            await ctx.send(f"Вы были успешно зарегистрированы, теперь можете отправить команды повторно")


def setup(bot):
    bot.add_cog(Data(bot))