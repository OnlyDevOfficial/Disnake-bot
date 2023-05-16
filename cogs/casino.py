from disnake.ext import commands
from db import DataBase
import disnake
import random

class Casino(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Хочешь проиграть все деньги?")
    async def casino(self , ctx , bet: int , number: str = commands.Param(
        name="number",
        choices=[
            "red",
            "black",
            "1st",
            "2st",
            "3st",
        ]
    )):
        user_name , balance , level , exp = self.DataBase.data(ctx.author.id)
        if balance > bet:
            red = [1 , 3 , 5 , 7 , 9 , 12 , 14 , 16 , 18 , 19 , 21 , 23 , 25 , 27 , 30 , 32 , 34 , 36]
            black = [2 , 4 , 6 , 8 , 10 , 11 , 13 , 15 , 17 , 20 , 22 , 24 , 26 , 28 , 29 , 31 , 33 , 35]
            one = [1 , 4 , 7 , 10 , 13 , 16 , 19 , 22 , 25 , 28 , 31 , 34]
            two = [2 , 5 , 8 , 11 , 14 , 17 , 20 , 23 , 26 , 29 , 32 , 35]
            three = [3 , 6 , 9 , 12 , 15 , 18 , 21 , 24 , 27 , 30 , 33 , 36]
            if number == "red":
                int = random.randint(1 , 36)
                if int in red:
                    self.DataBase.casino(ctx.author.id , bet , True)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Выигрыш",
                        description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                        )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                else:
                    self.DataBase.casino(ctx.author.id , bet , False)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Проигрыш",
                        description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                    )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

            if number == "black":
                int = random.randint(1 , 36)
                if int in black:
                    self.DataBase.casino(ctx.author.id , bet , True)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Выигрыш",
                        description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                        )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                else:
                    self.DataBase.casino(ctx.author.id , bet , False)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Проигрыш",
                        description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                    )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)


            if number == "1st":
                int = random.randint(1 , 36)
                if int in one:
                    self.DataBase.casino(ctx.author.id , bet , True)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Выигрыш",
                        description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                        )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                else:
                    self.DataBase.casino(ctx.author.id , bet , False)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Проигрыш",
                        description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                    )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                
            if number == "2st":
                int = random.randint(1 , 36)
                if int in two:
                    self.DataBase.casino(ctx.author.id , bet , True)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Выигрыш",
                        description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                        )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                else:
                    self.DataBase.casino(ctx.author.id , bet , False)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Проигрыш",
                        description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                    )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)


            if number == "3st":
                int = random.randint(1 , 36)
                if int in three:
                    self.DataBase.casino(ctx.author.id , bet , True)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Выигрыш",
                        description=f"Поздравляю! Вы выиграли {bet * 2}🍬\nВыпавшее число {int}"
                        )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

                else:
                    self.DataBase.casino(ctx.author.id , bet , False)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Проигрыш",
                        description=f"Сожалею , но вы проиграли {bet}🍬\nВыпавшее число {int}"
                    )
                    embed.set_image("https://media.discordapp.net/attachments/988531099758125107/1010301954620149810/ba6e304a67d26bbc.png?width=1025&height=419")
                    await ctx.send(embed=embed)

        else:
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Недостаточно средств",
                description=f"На вашем счету недостаточно средств!"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Casino(bot))