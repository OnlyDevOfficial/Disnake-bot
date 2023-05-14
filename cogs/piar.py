import disnake
from typing import Optional
from disnake.ext import commands
from disnake import TextInputStyle
import config

class Form_Command(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    class Form(disnake.ui.Modal):
        def __init__(self):
            components = [
                disnake.ui.TextInput(
                    label="Описание",
                    placeholder="Описание вашего сервера",
                    custom_id="Текст",
                    style=TextInputStyle.paragraph,
                ),

                disnake.ui.TextInput(
                    label="Особенности",
                    placeholder="Особенности вашего сервера",
                    custom_id="Особенности",
                    style=TextInputStyle.paragraph,
                ),

                disnake.ui.TextInput(
                    label="Ссылка",
                    placeholder="Ссылка на ваш сервер",
                    custom_id="Ссылка",
                    style=TextInputStyle.paragraph,
                ),
            ]

            super().__init__(
                title="Embed",
                custom_id="Embed",
                components=components,
            )

        # async def callback(self, inter: disnake.ModalInteraction):
        #     embed = disnake.Embed(color=0xffffff)
        #     for key, value in inter.text_values.items():
        #         embed.add_field(
        #             name="",
        #             value=value[:1024],
        #             inline=False,
        #         )
        #     await inter.response.send_message(embed=embed)


        class Buttons(disnake.ui.View):
            def __init__(self):
                super().__init__(timeout=0)
                self.value = Optional[bool]

            @disnake.ui.button(label="➕" , style=disnake.ButtonStyle.green)
            async def add(self , button: disnake.ui.Button , inter: disnake.CommandInteraction):
                await inter.response.send_modal(modal=Form_Command.Form())
                

        async def callback(self, inter: disnake.ModalInteraction):
            embed = disnake.Embed(color=0xffffff)
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )

            view = Form_Command.Form.Buttons()

            await inter.response.send_message(embed=embed , view=view)


    @commands.slash_command(description="Создает начально сообщение для функции пиара")
    @commands.has_permissions(administrator=True)
    async def pr(self , ctx):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            description="Тут вы можете спокойно пиарится"
        )
        embed.set_image("https://avatars.dzeninfra.ru/get-zen_doc/4721711/pub_619f7e21012f035dd48b6fd9_619f811afd0e4f5c6cfa97f1/scale_1200")

        view = Form_Command.Form.Buttons()

        await ctx.send(embed=embed , view=view)


def setup(bot):
    bot.add_cog(Form_Command(bot))