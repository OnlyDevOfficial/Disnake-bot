import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Embed(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

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
    async def embed(inter: disnake.AppCmdInter):
        await inter.response.send_modal(modal=Embed.Modal())


def setup(bot):
    bot.add_cog(Embed(bot))