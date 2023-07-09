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
        if self.DataBase.check_settings_true_module(message.author.guild.name , "exp"):
            int = random.randint(1 , 5)
            if self.DataBase.check_user(message.author.id) == True:
                self.DataBase.exp(message.author.id , int)

            else:
                channel = self.bot.get_channel(1099672058004250735)
                self.DataBase.create(message.author.id , message.author.name , message.author.guild.name)

def setup(bot):
    bot.add_cog(Exp(bot))