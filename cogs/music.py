import disnake
import requests

from bs4 import BeautifulSoup as bs
from disnake.ext import commands
from getuseragent import UserAgent

class Play(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
    @commands.slash_command(description="Не хотите послушать музыку?")
    async def play(self , ctx , music):
        
        agent = UserAgent()
        
        url = f"https://www.drivemusic.club/?do=search&subaction=search&story={music}"
        
        headers = {'User-Agent': agent.Random()}
        req = requests.get(url , headers=headers)
        src = req.text
        soup = bs(src , "lxml")
        music_block = soup.find_all(class_="btn_player")
        amount = 0
        
        channel = ctx.author.voice.channel
        
        if not channel:
            return
        
        if music_block:

            for item in music_block:
                if amount == 0:
                    music_item = item.find("a")
                    if music_item:
                        music_href = music_item.get("data-url")

                amount = amount + 1
                
        else:
            music_href = "По вашему запросу ничего не найдено!"
           
        voice_state = ctx.guild.voice_client 
            
        if voice_state and voice_state.is_connected():
            
            if music_href != "По вашему запросу ничего не найдено!":
                if voice_state.is_playing():
                    voice_state.stop()
                audio_source = disnake.FFmpegOpusAudio(music_href , bitrate=256)
                voice_state.play(audio_source)
                
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Музыка",
                    description=f"Играет: {music}"
                )
                
                await ctx.send(embed=embed)
                
            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Ошибка",
                    description=music_href
                )
                
                await ctx.send(embed=embed)
                
                voice_state = ctx.guild.voice_client
                
                await voice_state.disconnect()
                
        else:
            
            await channel.connect()
            
            voice_state = ctx.guild.voice_client
            
            if music_href != "По вашему запросу ничего не найдено!":
                audio_source = disnake.FFmpegOpusAudio(music_href)
                voice_state.play(audio_source)
                
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title="Музыка",
                    description=f"Играет: {music}"
                )
                
                await ctx.send(embed=embed)
                
            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="Ошибка",
                    description=music_href
                )
                
                await ctx.send(embed=embed)
                
                await voice_state.disconnect()
        

class Stop(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
        
    @commands.slash_command(description="Остановите! Я не хочу это слушать")
    async def stop(self , ctx):
        voice_state = ctx.guild.voice_client
        if voice_state.is_playing():
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Стоп",
                description="Музыка была остановлена"
            )
                    
            await ctx.send(embed=embed)
                    
            voice_state = ctx.guild.voice_client
                    
            await voice_state.disconnect()
        

class Pause(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
    @commands.slash_command(description="Пауза, хотя зачем я это объясняю")
    async def pause(self , ctx):
        voice_state = ctx.guild.voice_client
        if voice_state:
            voice_state.pause()
            
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Пауза",
                description="Вы поставили музыку на паузу"
            )
            
            await ctx.send(embed=embed)
            
        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Ошибка",
                description="Для начала включите какую нибудь песню!"
            )
            
            await ctx.send(embed=embed)
        
        
class Resume(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        
    @commands.slash_command(description="Отключить паузу, хотя зачем я это объясняю")
    async def resume(self , ctx):
        voice_state = ctx.guild.voice_client
        if voice_state:
            voice_state.resume()
            
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="Resume",
                description="Вы сняли музыку с паузы"
            )
            
            await ctx.send(embed=embed)
    
    
        
def setup(bot):
    bot.add_cog(Stop(bot))
    bot.add_cog(Play(bot))
    bot.add_cog(Pause(bot))
    bot.add_cog(Resume(bot))