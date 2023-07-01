import disnake
import json
import requests
from disnake.ext import commands
from db import DataBase
import datetime

class Binary(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Преобразовывает текст в бинарный код")
    async def binary(self , ctx , text):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            try:
                url = f"https://api.popcat.xyz/encode?text={text}"
                req = requests.get(url)
                res = json.loads(req.text)
                
                embed = disnake.Embed(
                    title="Бинарный код",
                    description=f"Результат преобразования текста `{text}` в бинарный код\n\n{res['binary']}",
                    color=disnake.Color.green()
                )
                
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")
                
                await ctx.send(embed=embed)
                
            except:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Error",
                    description="Произошла какая-то ошибка"
                )
                
                await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(Binary(bot))