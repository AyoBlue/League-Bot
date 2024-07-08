"""
Contains the following commands.

/offer <member>
    member: discord.Member
/release <member>
    member: discord.Member
/promote <member> <role>
    member: discord.Member
    role: discord.Role
/demote <member>
    member: discord.Member
/demand
"""

import disnake as discord
from disnake.ext import commands
from data import client

class Transactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Transactions(bot))