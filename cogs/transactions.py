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

from typing import Union
import disnake as discord
from disnake.ext import commands
from data import config

class Transactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        description = 'Offer a player to your team!',
        guild_ids = [config['server']],
        options = [
            discord.Option(name='member', description='Provide a member!', type=discord.OptionType.user, required=True)
        ]
    )
    async def offer(self, interaction: discord.ApplicationCommandInteraction, member: Union[discord.Member, discord.User]):
        ...

    @commands.slash_command(
        description = 'Release a player from your team!',
        guild_ids = [config['server']],
        options = [
            discord.Option(name='member', description='Provide a member!', type=discord.OptionType.user, required=True)
        ]
    )
    async def release(self, interaction: discord.ApplicationCommandInteraction, member: Union[discord.Member, discord.User]):
        ...

    @commands.slash_command(
        description = 'Promote a player on your team!',
        guild_ids = [config['server']],
        options = [
            discord.Option(name='member', description='Provide a member!', type=discord.OptionType.user, required=True),
            discord.Option(name='position', description='Choose a position!', type=discord.OptionType.role, required=True)
        ]
    )
    async def promote(self, interaction: discord.ApplicationCommandInteraction, member: Union[discord.Member, discord.User], role: discord.Role):
        ...

    @commands.slash_command(
        description = 'Demote a players position!',
        guild_ids = [config['server']],
        options = [
            discord.Option(name='member', description='Provide a member!', type=discord.OptionType.user, required=True)
        ]
    )
    async def demote(self, interaction: discord.ApplicationCommandInteraction, member: Union[discord.Member, discord.User]):
        ...

    @commands.slash_command(
        description = 'Demand from your team!',
        guild_ids = [config['server']]
    )
    async def demand(self, interaction: discord.ApplicationCommandInteraction):
        ...

def setup(bot):
    bot.add_cog(Transactions(bot))