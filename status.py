import discord
from discord.ext import commands
import aiohttp
import asyncio
from datetime import datetime
from colorama import Fore
import os
import json
from pystyle import Colors, Colorate

# Setup Discord client with proper intents
intents = discord.Intents.default()
intents.presences = False
intents.members = False

aizer = commands.Bot(command_prefix="!", intents=intents)

# Load config safely
with open('config.json', 'r') as f:
    config = json.load(f)
    statuses = config.get('statuses', [])
    token = config.get('Token', [])[0] if config.get('Token') else None
    rtsec = 0.0001

if not token:
    raise ValueError("Discord token not found in config.json")

# Clear screen safely
try:
    os.system("cls" if os.name == "nt" else "clear")
except:
    pass

# Display banner
print(Colorate.Vertical(Colors.blue_to_cyan, """

███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗         
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝         
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗         
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║         
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║         
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝         
                                                                                                            
Developed by @aesthetic.aizer#0 | Discord: /rexa | GitHub: AxZeRxD
"""))

# Status rotation function
async def koderstatus(client, token, statuses, rtsec):
    url = "https://discord.com/api/v8/users/@me/settings"

    while True:
        for status in statuses:
            payload = {
                "status": "online",
                "custom_status": {"text": status}
            }
            async with aiohttp.ClientSession() as session:
                async with session.patch(url, headers={'authorization': token}, json=payload) as response:
                    if response.status != 200:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] Failed to update status (Code: {response.status})")
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S')}] "
                              f"{Fore.LIGHTGREEN_EX}Status rotated → {Fore.LIGHTCYAN_EX}{status}{Fore.RESET}")
            await asyncio.sleep(rtsec)

# On ready event
@aizer.event
async def on_ready():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass
    print(Colorate.Vertical(Colors.blue_to_cyan, f"Logged in as {aizer.user}
Starting status rotator..."))
    await koderstatus(aizer, token, statuses, rtsec)

# Run bot
aizer.run(token)