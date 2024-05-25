Filename: moderation_bot/commands/delete_message.py

# Import necessary modules
import discord
from discord.ext import commands

# Import required files
from ..utils.error_handling import log_error

# Define the DeleteMessage cog
class DeleteMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to delete a message
    @commands.command(name='delete', help='Delete a message from the channel')
    async def delete_message(self, ctx, message_id: int):
        try:
            channel = ctx.channel
            message = await channel.fetch_message(message_id)
            await message.delete()
            await ctx.send(f'Message with ID {message_id} has been deleted successfully.')
        except discord.errors.NotFound:
            await ctx.send('Message not found. Please provide a valid message ID.')
        except discord.errors.Forbidden:
            await ctx.send('I do not have permission to delete this message.')
        except Exception as e:
            await log_error(e)
            await ctx.send('An error occurred while trying to delete the message.')

# Setup function to add the cog to the bot
def setup(bot):
    bot.add_cog(DeleteMessage(bot))

# Explanation: 
# This file contains the DeleteMessage cog, which includes a command to delete a message from the channel.
# It utilizes the error_handling.py file to log any errors that occur during message deletion.
# The cog is added to the bot in the setup function.