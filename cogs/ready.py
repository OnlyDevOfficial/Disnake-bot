import disnake
from disnake.ext import commands
import config

class Ready(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is ready to work")


def setup(bot):
    bot.add_cog(Ready(bot))