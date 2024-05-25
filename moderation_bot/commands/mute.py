Filename: mute.py

# Import necessary libraries
import discord
from discord.ext import commands

# Create a class for the Mute command
class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Mute command
    @commands.command(name='mute')
    async def mute(self, ctx, member: discord.Member):
        # Check if the user has the necessary permissions to mute members
        if ctx.author.guild_permissions.manage_roles:
            # Get the muted role
            muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
            
            if not muted_role:
                # Create the muted role if it doesn't exist
                muted_role = await ctx.guild.create_role(name='Muted')
                
                # Set permissions for the muted role
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted_role, send_messages=False)
            
            # Mute the member
            await member.add_roles(muted_role)
            await ctx.send(f'{member.mention} has been muted.')
        else:
            await ctx.send('You do not have permission to use this command.')

# Setup function to setup the Mute cog
def setup(bot):
    bot.add_cog(Mute(bot))

# Explanation: 
# The mute command allows server administrators to mute a specific member by assigning the 'Muted' role to them.
# If the 'Muted' role does not exist, the command creates it and sets permissions to restrict the member from sending messages.
# The function checks if the user running the command has the necessary permissions to mute members. If not, it sends a message indicating the lack of permission.