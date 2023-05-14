import disnake
from disnake.ext import commands
from disnake.interactions import MessageInteraction
import config

class Commands(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    class Menu(disnake.ui.StringSelect):

        def __init__(self):
            options = [
                disnake.SelectOption(label="Роли" , description="Показывает все роли сервера"),
                disnake.SelectOption(label="Правила" , description="Показывает правила сервера")
            ]

            super().__init__(
                placeholder="Menu",
                min_values=1,
                max_values=1,
                options=options
            )

        async def callback(self, inter: MessageInteraction):
            if self.values[0] == "Роли":
                embed = disnake.Embed(
                    color=0xffffff,
                    description=config.data['roles'],
                    title='Роли'
                )

                await inter.response.send_message(embed=embed , ephemeral=True)

            elif self.values[0] == "Правила":
                embed = disnake.Embed(
                    color=0xffffff,
                    description=config.data['rules'],
                    title='Правила'
                )
                await inter.response.send_message(embed=embed , ephemeral=True)
                

    class View(disnake.ui.View):

        def __init__(self):
            super().__init__()
            self.add_item(Commands.Menu())


    @commands.command()
    async def menu(self , ctx):
        embed = disnake.Embed(
            color=0xffffff,
        )
        embed.set_image("https://thumbs.dreamstime.com/b/картина-навигации-вектора-с-словом-предпосылка-114976893.jpg")
        await ctx.send(embed=embed , view=Commands.View())


def setup(bot):
    bot.add_cog(Commands(bot))