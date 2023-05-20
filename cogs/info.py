import disnake
from disnake.ext import commands
import config

class Info(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Информация о нашем сервере")
    async def guild_info(self , ctx):
        avatar = ctx.guild.icon.url
        member_avatar = ctx.author.display_avatar.url
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Информация о сервере __Folzy | Team__",
            description=f"**Название** - {ctx.guild.name}\n\n{config.data['guild']}\n\nУчастники сервера: {ctx.guild.member_count}"
        )

        embed.set_image(avatar)
        embed.set_thumbnail(member_avatar)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))