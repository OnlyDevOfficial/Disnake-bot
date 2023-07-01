from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Work(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Пахай негр")
    @commands.cooldown(1, 60*60*12 , commands.BucketType.user)
    async def work(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            username , bank , balance , level , work = self.DataBase.data(ctx.author.id)
            if work == 'Кассир':
                win = random.randint(3000 , 10000)

            elif work == 'Телеведущий':
                win = random.randint(10000 , 20000)

            elif work == 'Банкир':
                win = random.randint(30000 , 40000)
            # add_time = None
            self.DataBase.work(win , ctx.author.id)
            # self.DataBase.add_time_work(ctx.author.id , )
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Работа",
                description=f"Пользователь __{ctx.author.name}__ заработал {win}🍬"
            )
            date = datetime.datetime.now()
            embed.set_footer(text=f"{date}")
            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Work(bot))