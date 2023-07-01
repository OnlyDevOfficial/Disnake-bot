import disnake
from disnake.ext import commands
from db import DataBase
from disnake import TextInputStyle
import config

class Clear(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Эта команда удаляет сообщения в чате")
    @commands.has_permissions(administrator=True)
    async def clear(self , ctx , amount: int):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "admin_commands"):
        
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Удалено {amount} сообщений")
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды администрации отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Clear(bot))