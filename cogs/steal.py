from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Steal(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.persistents_view_added = False
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Я вызываю полицию")
    @commands.cooldown(1, 60*60*12 , commands.BucketType.user)
    async def steal(self , ctx , user: disnake.Member):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            username , balance , level , bank , work = self.DataBase.data(user.id)
            win = random.randint(0 , balance / 2)
            result = self.DataBase.steal(ctx.author.id , user.id , win)
            if result == "На счету жертвы не больше 4000🍬":
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    description=f"На счету пользователя не больше 4000🍬"
                )
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")

                await ctx.send(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Успех",
                    description=f"Вы успешно своровали {win}🍬 у {user.mention}"
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
    bot.add_cog(Steal(bot))