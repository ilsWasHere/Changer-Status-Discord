import requests
import time
import os
from colorama import init, Fore

def userinfo(token):
    header = {
        'authorization': token
    }
    r = requests.get("https://discord.com/api/v10/users/@me", headers=header)
    if r.status_code == 200:
        user_info = r.json()
        return user_info["username"], True
    else:
        return "Invalid token", False

def change_status(token, message, status):
    header = {
        'authorization': token
    }

    singapore = requests.get("https://discord.com/api/v10/users/@me/settings", headers=header).json()

    singapore2 = singapore.get("custom_status")
    if not isinstance(singapore2, dict):
        singapore2 = {}

    singapore2["text"] = message

    activities = singapore.get("activities", [])
    
    if status == "watching":
        activities = [{
            "name": message,
            "type": 3
        }]
    else:
        activities = [{
            "name": message,
            "type": 0  
        }]
    
    jsonData = {
        "custom_status": singapore2,
        "activities": activities,
        "status": status
    }

    r = requests.patch("https://discord.com/api/v10/users/@me/settings", headers=header, json=jsonData)
    return r.status_code

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def color(text, color_code):
    return f"{color_code}{text}{Fore.RESET}"

def banner():
    clear_console()

    print(f"""{Fore.RED}

   $$\           $$$$$$\            $$\  $$$$$$\  
 $$$$$$\        $$  __$$\           $$ |$$  __$$\ 
{Fore.LIGHTRED_EX}$$  __$$\       $$ /  \__| $$$$$$\  $$ |$$ /  \__|
{Fore.RED}$$ /  \__|      \$$$$$$\  $$  __$$\ $$ |$$$$\     
{Fore.LIGHTRED_EX}\$$$$$$\         \____$$\ $$$$$$$$ |$$ |$$  _|    
{Fore.RED} \___ $$\       $$\   $$ |$$   ____|$$ |$$ |      
$$\  \$$ |      \$$$$$$  |\$$$$$$$\ $$ |$$ |      
\$$$$$$  |       \______/  \_______|\__|\__|      
 \_$$  _/                                         

       {Fore.MAGENTA}Discord Status Changer by: ils
{Fore.RESET}
""")

token = '' # put your token
status = ["online", "idle", "dnd"] 
sleep = 2 # change sleep

statuses = [ 
    "test",
    "test1",
    "test2",
    "test3", # Write your status
    "test4",
    "test5",
    "test6"
]

count = 0
reset = time.time()

if not statuses:
    print("Err: No statuses")
    exit()   

banner()

while True:
    new_status = status[count % len(status)]
    log = statuses[count % len(statuses)]

    user_info, is_valid_token = userinfo(token)
    usercolor = Fore.GREEN if is_valid_token else Fore.RED
    token_info = f"{user_info}"
    color2 = color(token_info, usercolor)
    color3 = color(log, Fore.CYAN)

    print(f"{Fore.CYAN}User changed: {color2} | → {color3} | Status: {new_status}")
    change_status(token, log, new_status)
    
    count += 1

    time_reset = time.time()

    if time_reset - reset >= 10:
        banner()
        reset = time_reset

    time.sleep(sleep)
