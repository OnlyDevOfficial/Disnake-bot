import disnake
from disnake.ext import commands
from db import DataBase
import config
import random

class Members(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.Cog.listener()
    async def on_member_join(self , member):
        
        if self.DataBase.check_settings_true_module(member.guild.name , "greeting"):
            
            if self.DataBase.check_id_channel(member.guild.name , "greeting") != "False":
                try:
                    id = self.DataBase.check_id_channel(member.guild.name , "greeting")
                
                    channel = self.bot.get_channel(int(id))
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Приветствие 🤝",
                        description=f"{member.mention} ,приветствуем тебя на этом сервере. Прошу тебя зайти на канал с правилами и прочитать их, а так же на этом канале ты можешь ознакомится с другой информацией о этом сервере"
                    )
                    embed.set_image(file=disnake.File("greeting.gif"))

                    await channel.send(embed=embed)
                    
                except:
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="Ошибка",
                        description="Произошла какая-та ошибка"
                    )


    @commands.Cog.listener()
    async def on_member_remove(self , member):
        
        if self.DataBase.check_settings_true_module(member.guild.name , "farewell"):
        
            if self.DataBase.check_id_channel(member.guild.name , "greeting"):
                try:
                    channel = self.bot.get_channel(1123558548010455041)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Прощание 👋",
                        description=f"Мы прощаемся с {member.mention}, надеюсь он еще присоединится к нам"
                    )
                    embed.set_image(file=disnake.File("goodbye.png"))

                    await channel.send(embed=embed)
                    
                except:
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="Ошибка",
                        description="Произошла какая-та ошибка"
                    )


def setup(bot):
    bot.add_cog(Members(bot))