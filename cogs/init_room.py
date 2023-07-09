import disnake
import datetime
from disnake.ext import commands
from db import DataBase

class Room(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Создать категорию для создания приватных комнат")
    async def init_room(self, ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "rooms"):
            guild = disnake.utils.get(self.bot.guilds , name=ctx.author.guild.name)
            category = await guild.create_category_channel("Приватные комнаты")
            self.DataBase.settings(ctx.author.guild.name , "id категории" , category.id)
            await guild.create_text_channel("управление-комнатами-yakuza", category=category)
            voice = await guild.create_voice_channel("создать", category=category)
            self.DataBase.settings(ctx.author.guild.name , "Комнаты" , voice.id)
                
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Успех",
                description="Все категории и каналы были успешно созданы!"
            )
                
            date = datetime.datetime.now()
            embed.set_footer(text=f"{date}")
                
            await ctx.send(embed=embed)
        
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Приватные комнаты отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Room(bot))