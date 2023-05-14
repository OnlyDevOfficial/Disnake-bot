import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Errors(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self , ctx , error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author} У вас не достаточно прав для использования этой команды")
        elif isinstance(error , commands.UserInputError):
            await ctx.send(f"Команда не распознана")


def setup(bot):
    bot.add_cog(Errors(bot))