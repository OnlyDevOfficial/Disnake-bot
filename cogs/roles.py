from disnake.ext import commands
from db import DataBase
import datetime
import config
import disnake
import random

# class Buttons(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#     @disnake.ui.button(label="Роль" , style=disnake.ButtonStyle.grey , custom_id="Роль")
#     async def role(self , button: disnake.ui.Button , inter: disnake.Integration):
#         role = inter.guild.get_role(1109036457265483818)
#         if role in inter.author.roles:
#             await inter.author.remove_roles(role)

#         else:
#             await inter.author.add_roles(role)



class Roles(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.persistents_view_added = False
        self.DataBase = DataBase("db.db")

    
    # @commands.slash_command(description="Роли")
    # async def roles(self , ctx):
    #     view = Buttons()
    #     embed = disnake.Embed(color=disnake.Color.green() , title="Роли")

    #     await ctx.send(embed=embed , view=view)


    # @commands.Cog.listener()
    # async def on_connect(self):
    #     if self.persistents_view_added:
    #         return
        
    #     self.bot.add_view(Buttons() , message_id=1109040693583806544)


def setup(bot):
    bot.add_cog(Roles(bot))