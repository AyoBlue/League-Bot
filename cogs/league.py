"""
"""

import disnake as discord
from disnake.ext import commands
from data import client

class League(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(League(bot))