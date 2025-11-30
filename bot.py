import discord
import os
from dotenv import load_dotenv
load_dotenv()

print("Lancement du bot...")
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("apagnan ça commence")

@bot.event
async def on_message(message: discord.Message):
    if message.content == 'bonjour':
        channel = message.channel
        await channel.send("bien le sang")     

bot.run(os.getenv('DISCORD_TOKEN'))