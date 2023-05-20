from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Guess(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Попробуй угадай!")
    async def guess(self , ctx , bet: int , number: int = commands.Param(
        name="number",
        choices=[
            1,
            2,
            3,
            4,
            5,
        ]
    )):
        int = random.randint(1 , 5)
        user_name , balance , level , bank , work = self.DataBase.data(ctx.author.id)
        if balance >= bet:
            if number == int:
                self.DataBase.guess(ctx.author.id , bet , True)
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Выигрыш",
                    description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                )

                await ctx.send(embed=embed)

            else:
                self.DataBase.guess(ctx.author.id , bet , False)
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Проигрыш",
                    description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                )

                await ctx.send(embed=embed)

        else:
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Недостаточно средств",
                description=f"На вашем счету недостаточно средств!"
            )
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Guess(bot))