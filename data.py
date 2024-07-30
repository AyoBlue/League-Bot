import disnake as discord
import json

class Player:
    def __init__(self, payload): # This will contain more information in the future.
        self.coach_role = payload.get('coach_role')
        self.team = payload.get('team')

config = json.load(open('config.json'))
teams = {} # Manually add in all your teams, the key should be the Role Name or ID, Value is the Emoji ID if there is one. If not, leave as "None"
coaches = {} # The key should be the Role Name or ID, and the value should be the abbreviation. Example: "Head Coach": "HC"

# Functions needed for League.

async def get_player_data(self, member: discord.Member) -> None:
    data = {}
    for role in member.roles:
        emoji_id = self.teams.get(role.name) or self.teams.get(role.id)
        if emoji_id:
            team = {
                'role': role
            }
            if not(emoji_id == 'None'):
                team['emoji'] = discord.utils.get(member.guild.emojis, id=emoji_id)

            data['team'] = team
            continue

        abbreviation = self.coaches.get(role.name) or self.coaches.get(role.id)
        if abbreviation:
            data['coach'] = {
                'role': role,
                'abbreviation': abbreviation
            }
            continue

    return None if list(data.keys()) == 0 else Player(data)