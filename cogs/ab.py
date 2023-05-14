import disnake
from disnake.ext import commands
import config

class Ab(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Выполняет математическую опперацию")
    async def ab(self , ctx , a: int , opperation , b: int):
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

def setup(bot):
    bot.add_cog(Ab(bot))