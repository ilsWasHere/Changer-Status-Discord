import requests
import time
import os
from colorama import init, Fore

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_console()
    print(f"""{Fore.RED}
    __               __   ______  
  _/  |_            /  | /      \ 
 / $$   \   ______  $$ |/$$$$$$  |
/$$$$$$  | /      \ $$ |$$ |_ $$/ 
$$ \__$$/ /$$$$$$  |$$ |$$   |    
$$      \ $$    $$ |$$ |$$$$/     
 $$$$$$  |$$$$$$$$/ $$ |$$ |      
/  \__$$ |$$       |$$ |$$ |      
$$    $$/  $$$$$$$/ $$/ $$/       
 $$$$$$/                          
   $$/                            
                                  
                  {Fore.MAGENTA}Status Changer :,v
             {Fore.CYAN}Created by: Slfz
{Fore.RESET}""")

def userinfo(token):
    headers = {'authorization': token}
    r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    if r.status_code == 200:
        return r.json()["username"], True
    else:
        return "Invalid Token", False

def change_status(token, message, status):
    headers = {'authorization': token}
    settings = requests.get("https://discord.com/api/v10/users/@me/settings", headers=headers).json()
    custom_status = settings.get("custom_status") or {}
    custom_status["text"] = message
    activities = [{"name": message, "type": 3 if status == "watching" else 0}]
    jsonData = {"custom_status": custom_status, "activities": activities, "status": status}
    requests.patch("https://discord.com/api/v10/users/@me/settings", headers=headers, json=jsonData)

token = ''  #Pone tu token aca anormal 
status_list = ["online", "idle", "dnd"]
statuses = ["Test1", "Test2", "Test3"] #Elige cualquier estado :Vvv
sleep_time = 3 #Elige el tiempo que quieras, o nose jodete

def main():
    while True:
        for i, message in enumerate(statuses):
            status = status_list[i % len(status_list)]
            
            user_name, valid = userinfo(token)
            display_user = user_name if valid else f"{Fore.RED}Invalid Token"

            print(f"[⛧] {display_user} | Status: {status} | Message: {message} ⛧")
            change_status(token, message, status)

            time.sleep(sleep_time)

            
            if i == len(statuses) - 1:
                clear_console()
                banner()

if __name__ == "__main__":
    banner()
    main()
