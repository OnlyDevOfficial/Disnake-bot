import disnake
from disnake.ext import commands
from db import DataBase
from disnake import TextInputStyle

class Modal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Text",
                custom_id="Text",
                style=TextInputStyle.paragraph,
                placeholder="Текст вашего сообщения"
            )
        ]

        super().__init__(
            title="News",
            custom_id="News",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            embed = disnake.Embed(color=0xffffff , title=f"Новости сервера __{inter.guild.name}__" , description=value[:1024])
            embed.set_image(file=disnake.File("folzy_team.png"))

        await inter.response.send_message(embed=embed)

class News(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Вы на канале РенТв и ваш приветствует Folzy")
    @commands.has_permissions(administrator=True)
    async def news(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "admin_commands"):
            await ctx.response.send_modal(Modal())
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды администрации отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(News(bot))