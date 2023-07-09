from disnake.ext import commands
from db import DataBase
import disnake
import datetime

class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @disnake.ui.button(label="Поддержать проект" , style=disnake.ButtonStyle.url , url="https://www.youtube.com")
    async def project(self , button: disnake.ui.Button , inter: disnake.Interaction):
        pass
    
    @disnake.ui.button(label="Помощь" , style=disnake.ButtonStyle.url , url="https://discord.gg/VcbuG7Ws9d")
    async def help(self , button: disnake.ui.Button , inter: disnake.Interaction):
        pass
    
    @disnake.ui.button(label="Invite me" , style=disnake.ButtonStyle.url , url="https://discord.com/api/oauth2/authorize?client_id=1124294401364074548&permissions=8&scope=bot%20applications.commands")
    async def invite(self , button: disnake.ui.Button , inter: disnake.Interaction):
        pass
        
class Stats(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        self.members = 0
        
    @commands.slash_command(description="Статистика бота")
    async def stats(self , ctx):
        for guild in self.bot.guilds:
            self.members = self.members + len(guild.members)
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Статистика бота",
            description=f"`Yakuza` - мультисерверный бот написанный на языке `python`\n\nВ боте присутствуют множество команд таких категорий как: экономика, модерация, система уровней, музыка, развлекательные команды, кастомные комнаты и т.д.\n\nБот присутствует на `{len(self.bot.guilds)}` серверах и уже им пользуются `{self.members}` человек\n\nРазработчик бота 👨‍💻 - `f01zy`"
        )
        
        date = datetime.datetime.now()
        embed.set_footer(text=f"{date}")
        
        # embed.set_image("https://phonoteka.org/uploads/posts/2021-05/1620119539_32-phonoteka_org-p-zadnii-fon-samurai-36.jpg")
        
        await ctx.send(embed=embed , view=Buttons())
            
def setup(bot):
    bot.add_cog(Stats(bot))