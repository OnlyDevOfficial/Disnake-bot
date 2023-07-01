import disnake
from db import DataBase
from disnake.ext import commands
import config

class Ab(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Выполняет математическую опперацию")
    async def ab(self , ctx , a: int , opperation , b: int):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            if opperation == "-":
                result = a - b
                await ctx.send(f"Результат: {result}")

            elif opperation == "+":
                result = a + b
                await ctx.send(f"Результат: {result}")

            elif opperation == "*":
                result = a * b
                await ctx.send(f"Результат: {result}")

            elif opperation == "/":
                if b != 0:
                    result = a / b
                    await ctx.send(f"Результат: {result}")

                else:
                    await ctx.send("На 0 делить нельзя ! Иди в школе учись !")
                    
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ab(bot))