import disnake
import datetime
from disnake.ext import commands
from db import DataBase
from disnake.interactions import MessageInteraction
from disnake import TextInputStyle

class Menu(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Модерация" , emoji="🃏"),
            disnake.SelectOption(label="Экономика" , emoji="💵"),
            disnake.SelectOption(label="Музыка" , emoji="🎵"),
            disnake.SelectOption(label="Приветствие" , emoji="🤝"),
            disnake.SelectOption(label="Прощание" , emoji="👋"),
            disnake.SelectOption(label="Пользовательские команды" , emoji="🗣"),
            disnake.SelectOption(label="Уровни" , emoji="🎒"),
            disnake.SelectOption(label="Комнаты" , emoji="💾"),
        ]
        
        super().__init__(
            custom_id="settings",
            min_values=1,
            max_values=1,
            placeholder="Настройки",
            options=options
        )
        
    async def callback(self, inter: MessageInteraction):
        embed = disnake.Embed(
            title="Выберите нужную вам функцию",
            description="Выберите нужный пункт",
            color=disnake.Color.green()
        )
        
        if self.values[0] == "Модерация":
            await inter.response.edit_message(embed=embed , view=Buttons("Модерация"))
        
        elif self.values[0] == "Экономика":
            await inter.response.edit_message(embed=embed , view=Buttons("Экономика"))
            
        elif self.values[0] == "Приветствие":
            await inter.response.edit_message(embed=embed , view=Buttons("Приветствие"))
            
        elif self.values[0] == "Прощание":
            await inter.response.edit_message(embed=embed , view=Buttons("Прощание"))
            
        elif self.values[0] == "Пользовательские команды":
            await inter.response.edit_message(embed=embed , view=Buttons("Пользовательские команды"))
            
        elif self.values[0] == "Уровни":
            await inter.response.edit_message(embed=embed , view=Buttons("Уровни"))
            
        elif self.values[0] == "Музыка":
            await inter.response.edit_message(embed=embed , view=Buttons("Музыка"))
            
        elif self.values[0] == "Комнаты":
            await inter.response.edit_message(embed=embed , view=Buttons("Комнаты"))
            
class Buttons(disnake.ui.View):
    def __init__(self , option):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.option = option
        
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.gray , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            title="Настройки",
            description="Выберите один из полей",
            color=disnake.Color.green()
        )
        
        date = datetime.datetime.now()
        embed.set_footer(text=f"{date}")
        view = disnake.ui.View(timeout=None)
        view.add_item(Menu())
        await inter.response.edit_message(embed=embed , view=view)
        
    @disnake.ui.button(label="Включить" , style=disnake.ButtonStyle.green , custom_id="on")
    async def on(self , button: disnake.ui.Button , inter: disnake.Interaction):
        if self.option == "Приветствие" or self.option == "Прощание":
            await inter.response.send_modal(Modal(self.option))
            
        else:
            self.DataBase.settings(inter.author.guild.name , self.option , "True")
            embed = disnake.Embed(
                title="Успех",
                description="Настройки были успешно обновлены!",
                color=disnake.Color.green()
            )
            await inter.response.edit_message(embed=embed , view=Back())
    
    @disnake.ui.button(label="Выключить" , style=disnake.ButtonStyle.red , custom_id="off")
    async def off(self , button: disnake.ui.Button , inter: disnake.Interaction):
        if self.option == "Комнаты":
            if self.DataBase.check_settings_true_module(inter.author.guild.name , "rooms"):
                category = self.DataBase.check_id_channel(inter.author.guild.name , "music_category")
                category = disnake.utils.get(inter.author.guild.categories , id=category)
                for channel in category.channels:
                    await channel.delete()
                    
                await category.delete()
                self.DataBase.settings(inter.author.guild.name , "Комнаты" , "False")
                self.DataBase.settings(inter.author.guild.name , "id категории" , "None")
                
        else: self.DataBase.settings(inter.author.guild.name , self.option , "False")
                
        embed = disnake.Embed(
            title="Успех",
            description="Настройки были успешно обновлены!",
            color=disnake.Color.green()
        )
        
        await inter.response.edit_message(embed=embed , view=Back())

class Back(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.gray , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            title="Настройки",
            description="Выберите один из полей",
            color=disnake.Color.green()
        )
        
        date = datetime.datetime.now()
        embed.set_footer(text=f"{date}")
        view = disnake.ui.View(timeout=None)
        view.add_item(Menu())
        await inter.response.edit_message(embed=embed , view=view)

class Modal(disnake.ui.Modal):
    def __init__(self , option):
        components = [
            disnake.ui.TextInput(
                label="Id",
                custom_id="Id",
                style=TextInputStyle.short,
                placeholder="Id канала"
            )
        ]

        super().__init__(
            title="Id",
            custom_id="Id",
            components=components,
        )
        
        self.DataBase = DataBase("db.db")
        self.option = option

    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            self.DataBase.settings(inter.author.guild.name , self.option , value[:1024])
            embed = disnake.Embed(
                title="Успех",
                description="Настройки были успешно обновлены!",
                color=disnake.Color.green()
            )

        await inter.response.edit_message(embed=embed , view=Back())

class Settings(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Настройки")
    @commands.has_permissions(administrator=True)
    async def settings(self , ctx):
        if not self.DataBase.check_settings(ctx.author.guild.name):
            self.DataBase.setup_settings(ctx.author.guild.name)
            
        embed = disnake.Embed(
            title="Настройки",
            description="Выберите один из полей",
            color=disnake.Color.green()
        )
        
        date = datetime.datetime.now()
        embed.set_footer(text=f"{date}")
        view = disnake.ui.View(timeout=None)
        view.add_item(Menu())
        await ctx.send(embed=embed , view=view)
    
def setup(bot):
    bot.add_cog(Settings(bot))