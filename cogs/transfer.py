from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Transfer(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Не переводи деньги мошенникам")
    async def transfer(self , ctx , member: disnake.Member , money: int):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            result = self.DataBase.transfer(ctx.author.id , member.id , money)
            if result == "Error":
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Недостаточно средств",
                    description=f"На вашем счету недостаточно средств"
                )

                await ctx.send(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Успех",
                    description=f"Вы успешно перевели {money}🍬 пользователю {member.mention}"
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
    bot.add_cog(Transfer(bot))