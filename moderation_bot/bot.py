filename: bot.py

# Import necessary libraries
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Load all modules
bot.load_extension('commands.mute')
bot.load_extension('commands.delete_message')
bot.load_extension('commands.warn')
bot.load_extension('utils.message_filter')
bot.load_extension('utils.user_monitoring')
bot.load_extension('utils.error_handling')

# Run the bot
bot.run(TOKEN)