import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from db import DataBase
import config

class Embed(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    class Modal(disnake.ui.Modal):
        def __init__(self):
            components = [
                disnake.ui.TextInput(
                    label="Текст",
                    placeholder="Текст вашего сообщения",
                    custom_id="Текст",
                    style=TextInputStyle.paragraph,
                ),
            ]

            super().__init__(
                title="Embed",
                custom_id="Embed",
                components=components,
            )

        async def callback(self, inter: disnake.ModalInteraction):
            for key, value in inter.text_values.items():

                embed = disnake.Embed(color=disnake.Color.green() , description=value[:1024])

            await inter.response.send_message(embed=embed)


    @commands.slash_command(description="С помощью этой команды можно отправить Embed сообщение")
    async def embed(self , inter: disnake.AppCmdInter):
        if self.DataBase.check_settings_true_module(inter.author.guild.name , "user_commands"):
            await inter.response.send_modal(modal=Embed.Modal())
            
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Пользовательские команды отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Embed(bot))