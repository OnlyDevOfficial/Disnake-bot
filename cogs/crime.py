import disnake
import config
import random
import datetime
from disnake.ext import commands
from db import DataBase

class Crime(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')

    @commands.slash_command(description="Не попадись полиции!")
    @commands.cooldown(1, 60*60*12 , commands.BucketType.user)
    async def crime(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            win = [True , True , False]
            win = random.choice(win)
            money = random.randint(4000 , 12000)
            if win == True:
                self.DataBase.crime(ctx.author.id , money , True)
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Успех",
                    description=f"{random.choice(config.data['crime-win'])}{money}🍬"
                )
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")

                await ctx.send(embed=embed)

            else:
                self.DataBase.crime(ctx.author.id , money , False)

                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Вас поймали",
                    description=f"{random.choice(config.data['crime-lose'])}{money}🍬"
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
    bot.add_cog(Crime(bot))