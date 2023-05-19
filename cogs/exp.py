import disnake
import config
import random
from disnake.ext import commands
from db import DataBase

class Exp(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')

    @commands.Cog.listener()
    async def on_message(self , message):
        int = random.randint(1 , 5)
        if self.DataBase.check_user(message.author.id) == True:
            self.DataBase.exp(message.author.id , int)
            level = self.DataBase.level_up(message.author.id)
            if level == False:
                return
            
            else:
                user_name , balance , level_user , exp = self.DataBase.data(message.author.id)
                channel = self.bot.get_channel(1099672058004250735)
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Новый уровень",
                    description=f"Поздравляю! Пользователь __{user_name}__ повысил свой уровень , теперь его уровень: {level_user}"
                )

                await channel.send(embed=embed)

        else:
            channel = self.bot.get_channel(1099672058004250735)
            self.DataBase.create(message.author.id , message.author.name)

def setup(bot):
    bot.add_cog(Exp(bot))