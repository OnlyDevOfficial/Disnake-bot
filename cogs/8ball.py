import disnake
import json
import requests
from disnake.ext import commands
from db import DataBase

class Ball(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Спроси что-нибудь у 8ball")
    async def ball(self , ctx , query):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "user_commands"):
            try:
                url = f"https://api.popcat.xyz/8ball"
                req = requests.get(url)
                res = json.loads(req.text)
                
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="8ball API"
                )
                
                embed.add_field("query" , query , inline=False)
                embed.add_field("8ball" , res["answer"] , inline=False)
                
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
    bot.add_cog(Ball(bot))