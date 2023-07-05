import disnake
from disnake.ext import commands
from db import DataBase
from disnake import TextInputStyle
import config

class Kick(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Кикает пользователей")
    @commands.has_permissions(kick_members=True , administrator=True)
    async def kick(self , ctx , member: disnake.Member , * , reason="Нарушение прав"):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "admin_commands"):
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Бан",
                description=f"Администратор {ctx.author.mention} исключил пользователя {member.mention} по причине : {reason}"
            )
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды администрации отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Kick(bot))