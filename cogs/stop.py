import disnake
import datetime
from disnake.ext import commands
from db import DataBase

class Stop(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')
        
        
    @commands.slash_command(description="Остановите! Я не хочу это слушать")
    async def stop(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "music"):
            voice_state = ctx.guild.voice_client
            if voice_state != None:
                if voice_state.is_playing() != None:
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="Стоп",
                        description="Музыка была остановлена, если вы хотите опять запустить музыку, то введите команду /play (music)"
                    )
                    
                    date = datetime.datetime.now()
                    embed.set_footer(text=f"{date}")
                            
                    await ctx.send(embed=embed)
                            
                    voice_state = ctx.guild.voice_client
                            
                    await voice_state.disconnect()
                
            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Ошибка",
                    description="Сейчас не играет никакая музыка"
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
    bot.add_cog(Stop(bot))