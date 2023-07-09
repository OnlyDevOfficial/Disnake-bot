import disnake
from disnake.ext import commands
from db import DataBase

class Redirect(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.Database = DataBase("db.db")
        
    @commands.Cog.listener()
    async def on_voice_state_update(self , member, before, after):
        if after.channel is not None and after.channel.id == int(self.Database.check_id_channel(member.guild.name , "rooms")):
            guild = member.guild
            category = self.Database.check_id_channel(member.guild.name , "music_category")
            category = guild.get_channel(category)
            global channel
            channel = await guild.create_voice_channel(name=member.name , category=category)
            await member.move_to(channel)
            
        if before.channel is not None and before.channel.id == channel.id:
            guild = member.guild
            channel = guild.get_channel(before.channel.id)
            channel_members = channel.members
            if len(channel_members) == 0:
                await channel.delete()
            
def setup(bot):
    bot.add_cog(Redirect(bot))