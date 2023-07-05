import disnake
from disnake.ext import commands
from db import DataBase

class Commands(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")  
        
    
    
def setup(bot):
    bot.add_cog(Commands(bot))