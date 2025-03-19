from PIL import Image
import discord
from discord import app_commands
import requests
import io
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

zamn = Image.open("assets/zamn.png")

@tree.command(
    name="zamnify",
    description="ZAMN!😍"
)
@app_commands.describe(image="image to zamnify!😍", )
async def zamnify(interaction: discord.interactions, image: discord.Attachment):

    zamnedImage = Image.open(requests.get(image, stream=True).raw)
    zamnedImage = zamnedImage.resize((250, 356))
    zamn.paste(zamnedImage, (255, 73))
    
    with io.BytesIO() as image_binary:
        zamn.save(image_binary, 'PNG')
        image_binary.seek(0)
        zfile = discord.File(fp=image_binary, filename='zamn.png')

    await interaction.response.send_message(file=zfile)

@bot.event
async def on_ready():
    await tree.sync()

if __name__ == '__main__':
    bot.run(TOKEN)