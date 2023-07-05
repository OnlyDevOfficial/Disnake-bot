import disnake
import datetime
from disnake import TextInputStyle , MessageInteraction
from disnake.ext import commands
from db import DataBase

class Modal(disnake.ui.Modal):
    def __init__(self , option , command , back):
        self.option = option
        self.DataBase = DataBase("db.db")
        self.command = command
        self.back = back
        
        if option == "title":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder=option
                )
            ]
            
        elif option == "description":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.paragraph,
                placeholder=option
                )
            ]
            
        elif option == "image":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Ссылка на картинку"
                )
            ]
            
        elif option == "button_name":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Укажите название кнопке"
                )
            ]
            
        elif option == "role":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Укажите id роли"
                )
            ]
            
        elif option == "role_select":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Укажите id роли"
                )
            ]
            
        elif option == "SelectName":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Укажите название вашей опции"
                )
            ]
            
        elif option == "SelectDecription":
            components = [
            disnake.ui.TextInput(
                label=option,
                custom_id=option,
                style=TextInputStyle.short,
                placeholder="Укажите описание вашей опции"
                )
            ]

        super().__init__(
            title=option,
            custom_id=option,
            components=components,
        )
        
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            
            if self.option == "title":
                self.DataBase.embed(inter.author.guild.name , self.command , "title" , value[:1024])
                
            elif self.option == "description":
                self.DataBase.embed(inter.author.guild.name , self.command , "description" , value[:1024])
                
            elif self.option == "image":
                self.DataBase.embed(inter.author.guild.name , self.command , "description" , value[:1024])
                
            elif self.option == "button_name":
                self.DataBase.button(inter.author.guild.name , self.command , "value" , value[:1024])
                
            elif self.option == "role":
                self.DataBase.button(inter.author.guild.name , self.command , "action" , "role" , value[:1024])
                
            elif self.option == "role_select":
                self.DataBase.select(inter.author.guild.name , self.command , "action" , "role" , value[:1024])
                
            elif self.option == "SelectName":
                self.DataBase.select(inter.author.guild.name , self.command , "name" , value[:1024])
                
            elif self.option == "SelectDecription":
                self.DataBase.select(inter.author.guild.name , self.command , "description" , value[:1024])
            
            embed = disnake.Embed(
                title="Успех",
                description=f"{self.option} был успешно добавлен",
                color=disnake.Color.green()
            )
            
            await inter.response.edit_message(embed=embed , view=Back(self.command , self.back))
    
class Style(disnake.ui.StringSelect):
    def __init__(self , command):
        self.command = command
        self.DataBase = DataBase("db.db")
        
        options = [
            disnake.SelectOption(label="green" , description="Кнопка зеленого цвета" , emoji="🥑"),
            disnake.SelectOption(label="gray" , description="Кнопка серого цвета" , emoji="🍪"),
            disnake.SelectOption(label="red" , description="Кнопка красного цвета" , emoji="🍓"),
        ]
        
        super().__init__(
            custom_id="style",
            placeholder="Стили",
            min_values=1,
            max_values=1,
            options=options
        )
        
    async def callback(self , inter: MessageInteraction):
        if self.values[0] == "green":
            self.DataBase.button(inter.author.guild.name , self.command , "style" , "green")
            
        elif self.values[0] == "gray":
            self.DataBase.button(inter.author.guild.name , self.command , "style" , "gray")
            
        elif self.values[0] == "red":
            self.DataBase.button(inter.author.guild.name , self.command , "style" , "red")
    
        embed = disnake.Embed(
            title="Успех",
            description=f"Цвет {self.values[0]} был добавлен",
            color=disnake.Color.green()
        )
            
        await inter.response.edit_message(embed=embed , view=Back(self.command , "button"))        

class Button(disnake.ui.View):
    def __init__(self , command):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.command = command
        
    @disnake.ui.button(label="Название кнопки" , style=disnake.ButtonStyle.green , custom_id="name")
    async def name(self , button: disnake.ui.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("button_name" , self.command , "button"))
        
    @disnake.ui.button(label="Стиль" , style=disnake.ButtonStyle.gray , custom_id="style")
    async def style(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Стили",
            description="Выберите стиль кнопки на свой вкус"
        )
        
        view = disnake.ui.View(timeout=None)
        view.add_item(Style(self.command))
        
        await inter.response.edit_message(embed=embed , view=view)
        
    @disnake.ui.button(label="Действие" , style=disnake.ButtonStyle.danger , custom_id="action")
    async def action(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Действие",
            description="Выберите какое действие будет выполнять ваша кнопка"
        )
        
        view = disnake.ui.View(timeout=None)
        view.add_item(Action(self.command , "button"))
        
        await inter.response.edit_message(embed=embed , view=view)
    
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.blurple , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Custom",
            description="Тут вы можете создать собственную команду совершенно `бесплатно`"
        )
            
        await inter.response.edit_message(embed=embed , view=Buttons(self.command))
        
        
class Action(disnake.ui.StringSelect):
    def __init__(self , command , object):
        self.command = command
        self.object = object
        
        options = [
            disnake.SelectOption(label="Выдача роли" , description="При нажатии на вашу кнопку будет выдаваться роль" , emoji="🌗"),
        ]
        
        super().__init__(
            custom_id="action",
            placeholder="Действия",
            min_values=1,
            max_values=1,
            options=options
        )
        
    async def callback(self , inter: MessageInteraction):
        if self.object == "button":
            if self.values[0] == "Выдача роли":
                await inter.response.send_modal(Modal("role" , self.command , "button"))
                
        elif self.object == "menu":
            if self.values[0] == "Выдача роли":
                await inter.response.send_modal(Modal("role_select" , self.command , "menu"))
        

class Embed(disnake.ui.View):
    def __init__(self , command):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.command = command
        
    @disnake.ui.button(label="Добавить title" , style=disnake.ButtonStyle.green , custom_id="title")
    async def title(self , button: disnake.ui.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("title" , self.command , "embed"))
    
    @disnake.ui.button(label="Добавить description" , style=disnake.ButtonStyle.gray , custom_id="description")
    async def description(self , button: disnake.ui.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("description" , self.command , "embed"))
    
    @disnake.ui.button(label="Добавить картинку" , style=disnake.ButtonStyle.red , custom_id="image")
    async def image(self , button: disnake.ui.Button , inter: disnake.Interaction):
        await inter.response.send_modal(Modal("image" , self.command , "embed"))

    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.blurple , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Custom",
            description="Тут вы можете создать собственную команду совершенно `бесплатно`"
        )
            
        await inter.response.edit_message(embed=embed , view=Buttons(self.command))

class Buttons(disnake.ui.View):
    def __init__(self , command):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.command = command
        
    @disnake.ui.button(label="Добавить embed" , style=disnake.ButtonStyle.green , custom_id="embed")
    async def title(self , button: disnake.ui.Button , inter: disnake.Interaction):
        self.DataBase.create_embed(inter.author.guild.name , self.command)
        self.DataBase.activate(inter.author.guild.name , self.command , "embed")
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Embed",
            description="Выберите нужный вам пункт"
        )
        
        await inter.response.edit_message(embed=embed , view=Embed(self.command))
    
    @disnake.ui.button(label="Добавить кнопку" , style=disnake.ButtonStyle.danger , custom_id="button")
    async def button(self , button: disnake.ui.Button , inter: disnake.Interaction):
        self.DataBase.create_button(inter.author.guild.name , self.command)
        self.DataBase.activate(inter.author.guild.name , self.command , "button")
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Embed",
            description="Выберите нужный вам пункт"
        )
        
        await inter.response.edit_message(embed=embed , view=Button(self.command))
    
    @disnake.ui.button(label="Добавить выпадающее меню" , style=disnake.ButtonStyle.green , custom_id="menu")
    async def menu(self , button: disnake.ui.Button , inter: disnake.Interaction):
        self.DataBase.activate(inter.author.guild.name , self.command , "menu")
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Embed",
            description="Выберите нужный вам пункт"
        )
        
        await inter.response.edit_message(embed=embed , view=Select(self.command))
    
    
class Select(disnake.ui.View):
    def __init__(self , command):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.command = command
        
    @disnake.ui.button(label="Добавить опцию" , style=disnake.ButtonStyle.blurple , custom_id="add")
    async def add(self , button: disnake.ui.Button , inter: disnake.Interaction):
        self.DataBase.create_select(inter.author.guild.name , self.command)
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Действие",
            description="Выберите какое нужное вам поле"
        )
        
        await inter.response.edit_message(embed=embed , view=SelectButtons(self.command))
        
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.blurple , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Custom",
            description="Тут вы можете создать собственную команду совершенно `бесплатно`"
        )
            
        await inter.response.edit_message(embed=embed , view=Buttons(self.command))
      
      
class SelectButtons(disnake.ui.View):
    def __init__(self , command):
        super().__init__(timeout=None)
        self.command = command
        self.DataBase = DataBase("db.db")
        
    @disnake.ui.button(label="Название опции" , style=disnake.ButtonStyle.danger , custom_id="name")
    async def name(self , button: disnake.ui.Button , inter: disnake.Integration):
        await inter.response.send_modal(Modal("SelectName" , self.command , "menu"))
        
        
    @disnake.ui.button(label="Описание опции" , style=disnake.ButtonStyle.green , custom_id="description")
    async def description(self , button: disnake.ui.Button , inter: disnake.Integration):
        await inter.response.send_modal(Modal("SelectDecription" , self.command , "menu"))
        
        
    @disnake.ui.button(label="Действие опции" , style=disnake.ButtonStyle.gray , custom_id="action")
    async def action(self , button: disnake.ui.Button , inter: disnake.Integration):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Действие",
            description="Выберите какое действие будет выполнять эта опция"
        )
        
        view = disnake.ui.View(timeout=None)
        view.add_item(Action(self.command , "menu"))
        
        await inter.response.edit_message(embed=embed , view=view)
        
    
class Back(disnake.ui.View):
    def __init__(self , command , back):
        super().__init__(timeout=None)
        self.DataBase = DataBase("db.db")
        self.command = command
        self.back = back
        
    @disnake.ui.button(label="Назад" , style=disnake.ButtonStyle.green , custom_id="back")
    async def back(self , button: disnake.ui.Button , inter: disnake.Interaction):
        if self.back == "embed":        
            view = Embed(self.command)
            
        elif self.back == "button":
            view = Button(self.command)
            
            
        elif self.back == "menu":
            view = SelectButtons(self.command)
        
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Embed",
            description="Выберите нужный вам пункт"
        )
        
        await inter.response.edit_message(embed=embed , view=view)
    
class Name(disnake.ui.Modal):
    def __init__(self):
        self.DataBase = DataBase("db.db")
        
        components = [
            disnake.ui.TextInput(
                label="Name",
                custom_id="Name",
                style=TextInputStyle.short,
                placeholder="Название команды(писать на английском!)"
            )
        ]
        
        super().__init__(
            title="Name",
            custom_id="Name",
            components=components,
        )
        
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title="Custom",
                description="Тут вы можете создать собственную команду совершенно `бесплатно`"
            )
            
            self.DataBase.command(inter.author.guild.name , value[:1024])
            await inter.send(embed=embed , view=Buttons(value[:1024]))

class Custom(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")
        
    @commands.slash_command(description="Создайте свою собственную команду")
    async def custom(self , ctx):
        await ctx.response.send_modal(Name())
        
        
def setup(bot):
    bot.add_cog(Custom(bot))