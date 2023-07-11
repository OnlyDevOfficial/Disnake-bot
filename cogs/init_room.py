import disnake
import datetime
from disnake.ext import commands
from db import DataBase

class Modal(disnake.ui.Modal):
    def __init__(self , option):
        self.option = option
        
        components = [
            disnake.ui.TextInput(
                label="Data",
                custom_id="data",
                style=disnake.TextInputStyle.short,
                max_length=10,
                placeholder="Data",
            )
        ]
        
        super().__init__(
            title="Кастомизация",
            custom_id="custom",
            components=components
        )
        
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            if self.option == "Name":
                if inter.author.voice != None:
                    try:
                        channel = inter.author.voice
                        await channel.channel.edit(name=value[:1024])
                        await inter.send("Название канала успешно обновлено!", ephemeral=True)
                        
                    except:
                        await inter.send("Error" , ephemeral=True)
                    
            elif self.option == "Value":
                if inter.author.voice != None:
                    try:
                        channel = inter.author.voice
                        await channel.channel.edit(user_limit=value[:1024])
                        await inter.send("Лимит пользователей успешно изменен!", ephemeral=True)
                        
                    except:
                        await inter.send("Error" , ephemeral=True)


class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        
    @disnake.ui.button(emoji="🖊" , custom_id="name" , style=disnake.ButtonStyle.gray)
    async def name(self , button: disnake.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("Name"))
        
    @disnake.ui.button(emoji="👪" , custom_id="value" , style=disnake.ButtonStyle.gray)
    async def value(self , button: disnake.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("Value"))

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
            text = await guild.create_text_channel("управление-комнатами-yakuza", category=category)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Управление комнатами yakuza",
                description="🖊 Изменить имя\n👪 Изменить количество мест"
            )
            view = Buttons()
            await text.send(embed=embed , view=view)
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