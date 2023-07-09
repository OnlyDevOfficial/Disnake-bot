import disnake
from disnake.ext import commands
from disnake import MessageInteraction
import config

class Menu(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Администрация" , emoji="📚"),
            disnake.SelectOption(label="Экономика" ,  emoji="📰"),
            disnake.SelectOption(label="Пользовательские команды" , emoji="🌉"),
        ]
        
        super().__init__(
            custom_id="Menu",
            placeholder="Выберите пункт",
            max_values=1,
            min_values=1,
            options=options
        )

    async def callback(self, inter: MessageInteraction):
            if self.values[0] == "Администрация":
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Администрация",
                    description="```/ban - выдать бан\n/kick - выдать кик\n/clear - очистить сообщения\n/news - создать новость```"
                )
                
                await inter.response.edit_message(embed=embed , view=Back())
            
            elif self.values[0] == "Экономика":
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Экономика",
                    description="```/profile - показывает ваш профиль\n/casino - игра в казино\n/guess - игра в угадай чило\n/to - положить или снять деньги с банка\n/steal - воровать\n/work - работать\n/transfer - перевести деньги\n/buy - купить роль\n/shop - магазин\n/leaderboard - пахари сервера```"
                )
                
                await inter.response.edit_message(embed=embed , view=Back())
                
            elif self.values[0] == "Пользовательские команды":
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Пользовательские команды",
                    description="```/ab - вычислить\n/embed - отправить embed сообщение\n/steam - узнать информацию об игре в стиме\n/morse_code - перевести текст в азбуку морзе\n/8ball - спросить что нибудь у 8ball```"
                )
                
                await inter.response.edit_message(embed=embed , view=Back())
                    
class Back(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.gray , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):    
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title=f"Yakuza Help Menu",
            description="**Категории**\n\n> ✅ Экономика\n> ✅ Администрация\n> ✅ Пользовательские команды"
        )
        view = disnake.ui.View(timeout=None)
        view.add_item(Menu())
        await inter.response.edit_message(embed=embed , view=view)
        
                
class Help(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Показывает все команды сервера")
    async def help(self , ctx):        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title=f"Yakuza Help Menu",
            description="**Категории**\n\n> ✅ Экономика\n> ✅ Администрация\n> ✅ Пользовательские команды"
        )
        view = disnake.ui.View(timeout=None)
        view.add_item(Menu())
        await ctx.send(embed=embed , view=view)


def setup(bot):
    bot.add_cog(Help(bot))