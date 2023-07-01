import disnake
import json
import requests
from disnake.ext import commands
from db import DataBase

class Morse_code(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Преобразовывает текст в азбуку морзе")
    async def morse_code(self , ctx , text):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            try:
                url = f"https://api.popcat.xyz/texttomorse?text={text}"
                req = requests.get(url)
                res = json.loads(req.text)
                
                embed = disnake.Embed(
                    title="Азбука морзе",
                    description=f"Результат преобразования текста `{text}`\n{res['morse']}",
                    color=disnake.Color.green()
                )
                
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
    bot.add_cog(Morse_code(bot))