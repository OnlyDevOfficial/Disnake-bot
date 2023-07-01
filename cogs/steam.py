import requests
import json
import disnake
from db import DataBase
import datetime
from disnake.ext import commands

class Steam(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Найти любую игру в стиме")
    async def steam(self , ctx , game):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            try:
                url = f"https://api.popcat.xyz/steam?q={game}"
                req = requests.get(url)
                res = req.text
                data = json.loads(res)
                
                if "error" in data:
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="Error",
                        description=data["error"]
                    )
                    
                    await ctx.send(embed=embed)
                    
                else:

                    embed = disnake.Embed(
                        title="Steam",
                        color=disnake.Color.green(),
                    )
                    
                    date = datetime.datetime.now()
                    embed.set_footer(text=f"{date}")
                    
                    embed.add_field(name="Название" , value=data["name"] , inline=False)
                    embed.add_field(name="Тип" , value=data["type"] , inline=False)
                    embed.add_field(name="Описание" , value=data["description"] , inline=False)
                    embed.add_field(name="Цена" , value=data["price"] , inline=False)
                    
                    embed.set_image(url=data["banner"])
            
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
    bot.add_cog(Steam(bot))