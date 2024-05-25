# main.py

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from config import settings
from bot import ModerationBot

# Load environment variables from .env file
load_dotenv()

# Initialize bot
bot = commands.Bot(command_prefix=settings['prefix'])
moderation_bot = ModerationBot(bot)

# Events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))