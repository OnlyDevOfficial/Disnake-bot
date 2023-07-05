import disnake
import requests
import io
import matplotlib.pyplot as plt
from disnake.ext import commands
from db import DataBase
from PIL import Image, ImageDraw , ImageFont , ImageFilter

class Level(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.DataBase = DataBase("db.db")

    @commands.slash_command(description="Показывает ваш уровень")
    async def level(self , ctx):
        exp = self.DataBase.exp_check(ctx.author.id)
        
        username , balance , level , bank , work = self.DataBase.data(ctx.author.id)
        
        img = Image.new("RGBA" , (400 , 130) , "black")
        url = ctx.author.display_avatar.url

        response = requests.get(url , stream=True)
        response = Image.open(io.BytesIO(response.content))
        response = response.convert("RGBA")
        response = response.resize((100 , 100) , Image.ANTIALIAS)
        
        blur_radius = 0
        offset = 4
        back_color = Image.new(response.mode, response.size, (0,0,0))
        offset = blur_radius * 2 + offset
        mask = Image.new("L", response.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((offset, offset, response.size[0] - offset, response.size[1] - offset), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

        response = Image.composite(response, back_color, mask)
        plt.imshow(response)
        
        img.paste(response , (15 , 15 , 115 , 115))
        
        draw = ImageDraw.Draw(img)
        
        font = ImageFont.truetype("arial.ttf" , size=20)

        draw.text((145 , 50) , f"{ctx.author.name}       Ур. {level}     {exp}/exp" , font = ImageFont.truetype("arial.ttf" , size=20))
        
        img.save("card.png")
        
        embed = disnake.Embed(
            color=disnake.Color.green()
        )
        
        embed.set_image(file=disnake.File("card.png"))
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Level(bot))