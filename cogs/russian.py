from disnake.ext import commands
from db import DataBase
from typing import Optional
import datetime
import config
import disnake
import random

class Russian(commands.Cog):
    def __init__(self , bot):
        self.bot = bot


    # class Buttons(disnake.ui.View):
    #     def __init__(self , bet: int , int: int , object):
    #         super().__init__(timeout=0)
    #         self.value = Optional[bool]
    #         self.bet = bet
    #         self.int = int
    #         self.bool_data = object
    #         self.DataBase = DataBase("db.db")

    #     @disnake.ui.button(label="Выстрел" , style=disnake.ButtonStyle.green)
    #     async def fire(self , button: disnake.ui.Button , inter: disnake.CommandInteraction):
    #         self.bool_data.pop(0)
    #         if self.bool_data[0] == "True":
    #             if self.int > self.bet / 6:
    #                 deb = round(self.bet / 6)
    #                 self.DataBase.debiting(inter.author.id , deb)
    #             global number
    #             number = round(self.int)
    #             self.DataBase.russian(inter.author.id , number , True)
    #             embed = disnake.Embed(
    #                 color=disnake.Color.green(),
    #                 title="Вы остальсь в живых",
    #                 description=f"На этот раз вам повезло , вы можете забрать выигрышь в сумме {self.bet + number}🍬"
    #             )

    #             await inter.send(embed=embed , view=Russian.Buttons(self.bet , round(self.int + self.bet / 6) , self.bool_data))

    #         else:
    #             self.DataBase.russian(inter.author.id , self.bet + number , False)
    #             embed = disnake.Embed(
    #                 color=disnake.Color.green(),
    #                 title="Вы совершили самоубийство",
    #                 description=f"Вам не повезло , и вы совершили самоубийство . Сумма проигрыша: {self.bet}🍬"
    #             )

    #             await inter.send(embed=embed)
                

    #     # @disnake.ui.button(label="Забрать" , style=disnake.ButtonStyle.green)
    #     # async def cancel(self , button: disnake.ui.Button , inter: disnake.CommandInteraction):
    #     #     self.DataBase.russian(inter.author.id , win , True)
    #     #     embed = disnake.Embed(
    #     #         color=disnake.Color.green(),
    #     #         title="Выигрышь",
    #     #         description=f"Вы сильно рисковали , но вам повезло . Сумма выигрыша: {win}"
    #     #     )

    #     #     await inter.send(embed=embed)
            


    # @commands.slash_command(description="Русская рулетка")
    # async def russian(self , ctx , bet: int):
    #     bool_data_list_1 = ["True" , "True" , "True" , "True" , "False"]
    #     bool_data_list = random.sample(bool_data_list_1 , len(bool_data_list_1))
    #     bool_data = ["True"] + bool_data_list
    #     print(bool_data)
    #     embed = disnake.Embed(
    #         color=disnake.Color.green(),
    #         title="Русская рулетка",
    #         description="Эта игра не на жизнь , а на смерть!"
    #     )
    #     await ctx.send(embed=embed , view=Russian.Buttons(bet , bet / 6 , bool_data))


def setup(bot):
    bot.add_cog(Russian(bot))