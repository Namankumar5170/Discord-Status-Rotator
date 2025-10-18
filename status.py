import discord 
from discord.ext import tasks, commands
import aiohttp
import random
import asyncio
from datetime import datetime
from colorama import Fore
import os 
import json
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

aizer = discord.Client()

with open('config.json') as f:
    config = json.load(f)
    statuses = config['statuses']
    rtsec = .0001
    token = config['Token'][0]

os.system("cls")

print(Colorate.Vertical(Colors.blue_to_cyan,(f"""

                                                        ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗         
                                                        ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝         
                                                        ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗         
                                                        ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║         
                                                        ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║         
                                                        ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝         
                                                                                                                
                                                    ██████╗  ██████╗ ████████╗ █████╗ ████████╗ ██████╗ ██████╗ 
                                                    ██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                                                    ██████╔╝██║   ██║   ██║   ███████║   ██║   ██║   ██║██████╔╝
                                                    ██╔══██╗██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║██╔══██╗
                                                    ██║  ██║╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██║
                                                    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    


                                                                    @aesthetic.aizer#0 - Dev
                                                                    @nukersop          - YouTube
                                                                    /rexa              - Discord
                                                                    AxZeRxD            - Github

\n\n\n""")))



async def koderstatus(token, statuses, rtsec):
    url = "https://discord.com/api/v8/users/@me/settings"


    while True:
        for status in statuses:
            jsonData = {
                "status": "online",
                "custom_status": {
                    "text": status,
                }
            }
            async with aiohttp.ClientSession() as session:
                async with session.patch(url, headers={'authorization': token}, json=jsonData) as response:
                    if response.status != 200:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] Failed to update status. Status code: {response.status}")
                    else:
                        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTMAGENTA_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTGREEN_EX} INFO {Fore.LIGHTBLACK_EX} TOKEN {Fore.LIGHTCYAN_EX} {token[:25]}***** {Fore.LIGHTBLACK_EX} ID {Fore.LIGHTCYAN_EX}{aizer.user.id} {Fore.LIGHTBLACK_EX}RESPONSE {Fore.LIGHTBLACK_EX} STATUS ROTATED {Fore.LIGHTBLACK_EX} STATUS {Fore.LIGHTCYAN_EX}{status} {Fore.RESET}")

        await asyncio.sleep(rtsec)



@aizer.event
async def on_ready():
    os.system(f"cls & title @aesthetic.aizer ^| Status Rotator ^| [discord.gg/rexa]")
    os.system("cls")
    print(Colorate.Vertical(Colors.blue_to_cyan,(f"""

                                                        ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗         
                                                        ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝         
                                                        ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗         
                                                        ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║         
                                                        ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║         
                                                        ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝         
                                                                                                                
                                                    ██████╗  ██████╗ ████████╗ █████╗ ████████╗ ██████╗ ██████╗ 
                                                    ██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                                                    ██████╔╝██║   ██║   ██║   ███████║   ██║   ██║   ██║██████╔╝
                                                    ██╔══██╗██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║██╔══██╗
                                                    ██║  ██║╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██║
                                                    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                    

                                                                    @aesthetic.aizer#0 - Dev
                                                                    @nukersop          - YouTube
                                                                    /rexa              - Discord
                                                                    AxZeRxD            - Github
                                                                    

\n\n\n""")))

    await koderstatus(token, statuses, rtsec)

aizer.run(token)
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