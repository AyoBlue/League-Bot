"""
"""

import disnake as discord
from disnake.ext import commands
from data import client

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(General(bot))