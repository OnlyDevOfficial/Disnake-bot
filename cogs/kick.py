import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Kick(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Кикает пользователей")
    @commands.has_permissions(kick_members=True , administrator=True)
    async def kick(self , ctx , member: disnake.Member , * , reason="Нарушение прав"):
        await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention} по причине : {reason}")
        await member.kick(reason=reason)


def setup(bot):
    bot.add_cog(Kick(bot))