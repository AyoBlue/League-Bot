import disnake as discord
from disnake.ext import commands
from data import client
from colorama import Fore
import sys
import os

bot = commands.Bot('$', case_insensitive=True, intents=discord.Intents().all())

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

os.system('cls' if sys.platform == 'win32' else 'clear')
try:
    bot.run(client.token)
except discord.errors.LoginFailure:
    print(f'{Fore.RED}Invalid Token!{Fore.RESET}')
except discord.errors.PrivilegedIntentsRequired:
    print(f'Intents {Fore.RED}NOT{Fore.RESET} enabled on Discord!')
except discord.errors.HTTPException:
    print(f'You are currently {Fore.RED}blocked{Fore.RESET} from accessing Discord\'s API due to excessive requests.')
except Exception as e:
    if e.__class__.__name__ == 'ClientConnectorCertificateError':
        print(f'Internet Connection {Fore.RED}blocked{Fore.RESET} from accessing {Fore.BLUE}Discord!{Fore.RESET}')