import disnake
import datetime
from disnake.ext import commands
from db import DataBase

class Resume(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')
        
    @commands.slash_command(description="Отключить паузу, хотя зачем я это объясняю")
    async def resume(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "music"):
            voice_state = ctx.guild.voice_client
            if voice_state:
                voice_state.resume()
                
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Resume",
                    description="Вы сняли музыку с паузы, чтобы опять поставить ее на паузу пропишите команду /pause"
                )
                
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")
                
                await ctx.send(embed=embed)
                
            else:
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Ошибка",
                    description="Вы не подключены ни к одному голосовому каналу!"
                )
                
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")
                
                await ctx.send(embed=embed)
    
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Музыка отключена на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(Resume(bot))