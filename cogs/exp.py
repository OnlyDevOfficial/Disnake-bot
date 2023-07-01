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
                level = self.DataBase.level_up(message.author.id)
                if level == False:
                    return
                
                else:
                    user_name , balance , level , bank , work = self.DataBase.data(message.author.id)
                    channel = self.bot.get_channel(1123559036999192727)


                    if level == 2:
                        await message.author.add_roles(message.guild.get_role(1099667894637432893))
                        await message.author.remove_roles(message.guild.get_role(1099667941479424070))
                        await message.author.remove_roles(message.guild.get_role(1099668066201247894))
                        await message.author.remove_roles(message.guild.get_role(1099668193871667300))
                        await message.author.remove_roles(message.guild.get_role(1099668274830131345))


                    if level == 5:
                        await message.author.add_roles(message.guild.get_role(1099667941479424070))
                        await message.author.remove_roles(message.guild.get_role(1099667894637432893))
                        await message.author.remove_roles(message.guild.get_role(1099668066201247894))
                        await message.author.remove_roles(message.guild.get_role(1099668193871667300))
                        await message.author.remove_roles(message.guild.get_role(1099668274830131345))


                    if level == 10:
                        await message.author.add_roles(message.guild.get_role(1099668066201247894))
                        await message.author.remove_roles(message.guild.get_role(1099667894637432893))
                        await message.author.remove_roles(message.guild.get_role(1099667941479424070))
                        await message.author.remove_roles(message.guild.get_role(1099668193871667300))
                        await message.author.remove_roles(message.guild.get_role(1099668274830131345))


                    if level == 20:
                        await message.author.add_roles(message.guild.get_role(1099668193871667300))
                        await message.author.remove_roles(message.guild.get_role(1099667894637432893))
                        await message.author.remove_roles(message.guild.get_role(1099667941479424070))
                        await message.author.remove_roles(message.guild.get_role(1099668066201247894))
                        await message.author.remove_roles(message.guild.get_role(1099668274830131345))


                    if level == 30:
                        await message.author.add_roles(message.guild.get_role(1099668274830131345))
                        await message.author.remove_roles(message.guild.get_role(1099667894637432893))
                        await message.author.remove_roles(message.guild.get_role(1099667941479424070))
                        await message.author.remove_roles(message.guild.get_role(1099668066201247894))
                        await message.author.remove_roles(message.guild.get_role(1099668193871667300))         

            
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title="Новый уровень",
                        description=f"Поздравляю! Пользователь __{user_name}__ повысил свой уровень , теперь его уровень: {level}"
                    )

                    await channel.send(embed=embed)

            else:
                channel = self.bot.get_channel(1099672058004250735)
                self.DataBase.create(message.author.id , message.author.name , message.author.guild.name)

def setup(bot):
    bot.add_cog(Exp(bot))