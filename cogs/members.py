import disnake
from disnake.ext import commands
import config

class Members(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self , member):
        channel = self.bot.get_channel(1099664405559513161)

        embed = disnake.Embed(
            title="Новый участник",
            description=f"Добро пожаловать на сервер {member.mention}",
            color=disnake.Color.green()
        )

        await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self , member):
        channel = self.bot.get_channel(1099665452092899418)

        embed = disnake.Embed(
            title="Прощание",
            description=f"прощай {member.mention}",
            color=disnake.Color.green()
        )

        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Members(bot))