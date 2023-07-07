from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

class Buy(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Не хочешь чего нибудь купить?")
    async def buy(self , ctx , name):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            for i in self.DataBase.shop(ctx.author.guild.name):
                if name in i:
                    result = self.DataBase.buy(name , ctx.author.id)
                    if result == "На вашем счету недостаточно средств!":
                        embed = disnake.Embed(
                            color=disnake.Color.red(),
                            title="Недостаточно средств",
                            description=result
                        )
                        
                        date = datetime.datetime.now()
                        embed.set_footer(text=f"{date}")

                        await ctx.send(embed=embed)

                    else:
                        guild = self.bot.get_guild(ctx.guild.id)
                        role = guild.get_role(result)
                        
                        await ctx.author.add_roles(role)

                        embed = disnake.Embed(
                            color=disnake.Color.green(),
                            title="Покупка",
                            description=f"Поздравляю! Вы приобрели роль {role}"
                        )
                        
                        date = datetime.datetime.now()
                        embed.set_footer(text=f"{date}")

                        await ctx.send(embed=embed)
                        
                else:
                    result = self.DataBase.shop(ctx.author.guild.name)
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="Ошибка",
                        description="Извините, но такого предмета нет в магазине, попробуйте посмотреть весь товар введя команду /shop"
                    )
                    print(f"[log] {result}")
                    
                    await ctx.send(embed=embed)
                
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Buy(bot))