import disnake
from disnake.ext import commands
import config
from db import DataBase

class Give(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Информация о нашем сервере")
    @commands.has_permissions(administrator=True)
    async def give(self , ctx , member: disnake.Member , amount: int):
        self.DataBase.give(member.id , amount)
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Успех",
            description=f"Вы успешно выдали {amount}🍬 пользователю {member.mention}"
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Give(bot))