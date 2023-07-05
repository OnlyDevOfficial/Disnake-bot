import disnake
from disnake.ext import commands
from disnake.interactions import MessageInteraction
import config
from db import DataBase

class Menu_Select(disnake.ui.StringSelect):

    def __init__(self):
        options = [
            disnake.SelectOption(label="Кассир" , description="30000🍬"),
            disnake.SelectOption(label="Телеведущий" , description="100000🍬"),
            disnake.SelectOption(label="Банкир" , description="300000🍬")
        ]

        super().__init__(
            placeholder="Вакансии",
            min_values=1,
            custom_id="Вакансии",
            max_values=1,
            options=options
        )

        self.DataBase = DataBase('db.db')

    async def callback(self, inter: MessageInteraction):
        if self.values[0] == "Кассир":
            user_name , balance , level , bank , work = self.DataBase.data(inter.author.id)
            if balance >= 30000:
                self.DataBase.hire(inter.author.id , "Кассир")
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    description="Вы успешно устроились на работу кассиром",
                    title='Работа'
                )

                await inter.response.send_message(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    description="На вашем счету недостаточно средств",
                    title='Недостаточно средств'
                )
                await inter.response.send_message(embed=embed)

        elif self.values[0] == "Телеведущий":
            user_name , balance , level , bank , work = self.DataBase.data(inter.author.id)
            if balance >= 100000:
                self.DataBase.hire(inter.author.id , "Телеведущий")
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    description="Вы успешно устроились на работу телеведущим",
                    title='Работа'
                )
                await inter.response.send_message(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    description="На вашем счету недостаточно средств",
                    title='Недостаточно средств'
                )
                await inter.response.send_message(embed=embed)

        elif self.values[0] == "Банкир":
            user_name , balance , level , bank , work = self.DataBase.data(inter.author.id)
            if balance >= 300000:
                self.DataBase.hire(inter.author.id , "Банкир")
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    description="Вы успешно устроились на работу банкиром",
                    title='Работа'
                )
                await inter.response.send_message(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    description="На вашем счету недостаточно средств",
                    title='Недостаточно средств'
                )
                await inter.response.send_message(embed=embed)



class Hired(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.persistents_view_added = False


    @commands.slash_command(description="Не нравится работа? Устройся на другую")
    @commands.has_permissions(administrator=True)
    async def hire(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Вакансии",
            )
            
            embed.set_image("http://oeildurecruteur.ca/wp-content/uploads/2020/04/shutterstock_1264167598.jpg")
            
            view = disnake.ui.View(timeout=None) 
            view.add_item(Menu_Select()) 
            await ctx.send(view=view)
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Hired(bot))