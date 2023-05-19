import disnake
from disnake.ext import commands
from disnake.interactions import MessageInteraction
import config

class Menu_Select(disnake.ui.StringSelect):

    def __init__(self):
        options = [
            disnake.SelectOption(label="Роли" , description="Показывает все роли сервера"),
            disnake.SelectOption(label="Правила" , description="Показывает правила сервера")
        ]

        super().__init__(
            placeholder="Информация о сервере",
            min_values=1,
            custom_id="menu",
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

class Menu(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.persistents_view_added = False


    @commands.slash_command(description="Создает меню навигации")
    @commands.has_permissions(administrator=True)
    async def menu(self , ctx):
        view = disnake.ui.View(timeout=None) 
        view.add_item(Menu_Select())  
        embed = disnake.Embed(
            color=disnake.Color.green(),
        )
        embed.set_image("https://media.discordapp.net/attachments/1092179374490521700/1100423154414911548/1000x2500_INFO.png?width=1025&height=410")
        await ctx.send(embed=embed , view=view)


    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_view_added:
            return
        
        view = disnake.ui.View(timeout=None) 
        view.add_item(Menu_Select())  
        self.bot.add_view(view , message_id=1109127069864054795)


def setup(bot):
    bot.add_cog(Menu(bot))