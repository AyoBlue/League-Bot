"""
"""

import disnake as discord
from disnake.ext import commands

class Background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Background(bot))