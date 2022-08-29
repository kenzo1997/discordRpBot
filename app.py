import os
import nextcord as discord
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print("Successfully booted the bot up!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run(token)
