import disnake
from disnake.ext import commands
import config

class Events(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is ready to work")

    @commands.Cog.listener()
    async def on_member_join(self , member):
        channel = self.bot.get_channel(1100086673448108103)

        embed = disnake.Embed(
            title="Новый участник",
            description=f"Добро пожаловать @{member.name}#{member.discriminator}",
            color=0xffffff
        )

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self , message):
        for content in message.content.split():
            for words in config.data["words"]:
                if words in content:
                    await message.delete()


def setup(bot):
    bot.add_cog(Events(bot))