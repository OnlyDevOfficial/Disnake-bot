import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Ban(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Кикает пользователей")
    @commands.has_permissions(kick_members=True , administrator=True)
    async def ban(self , ctx , member: disnake.Member , * , reason="Нарушение прав"):
        await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention} по причине : {reason}")
        await member.ban(reason=reason)


def setup(bot):
    bot.add_cog(Ban(bot))