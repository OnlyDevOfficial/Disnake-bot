import disnake
import config
from disnake.ext import commands
from db import DataBase
import datetime

class Data(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase('db.db')

    @commands.slash_command(description="Показывает ваш профиль")
    async def profile(self , ctx):
        if self.DataBase.check_settings_true_module(ctx.author.guild.name , "economy_commands"):
            if self.DataBase.check_user(ctx.author.id) == True:
                username , balance , level , bank , work = self.DataBase.data(ctx.author.id)
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title=f"__Информация о пользователе {username}__",
                    description=f"__{username}__ работает {work}\nНа его балансе сейчас {balance}🍬\nА в банке {bank}🍬"
                )
                
                date = datetime.datetime.now()
                embed.set_footer(text=f"{date}")

                await ctx.send(embed=embed)

            else:
                self.DataBase.create(ctx.author.id , ctx.author.name , ctx.author.guild.name)
                await ctx.send(f"Вы были успешно зарегистрированы, теперь можете отправить команды повторно")
                
        else:
            embed = disnake.Embed(
                title="Ошибка",
                description="Команды экономики отключены на вашем сервере! Чтобы включить их пропишите команду **/settings** и выберите нужный вам пункт",
                color=disnake.Color.red()
            )
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Data(bot))