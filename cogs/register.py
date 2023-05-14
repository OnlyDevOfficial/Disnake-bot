import disnake
import config
from disnake.ext import commands
from db import DataBase

class Register(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')

    @commands.Cog.listener()
    async def on_message(self , message):
        if self.DataBase.check_user(message.author.id) == True:
            pass

        else:
            channel = self.bot.get_channel(1100086673448108103)
            self.DataBase.create(message.author.id , message.author.name)
            await channel.send(f"Пользователь {message.author.mention} был успешно зарегистрирован в базе данных!")

def setup(bot):
    bot.add_cog(Register(bot))