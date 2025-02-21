import signal, sys, os, requests, json
from utils.banners import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    clear_screen()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_name(steam_id: int):

    try:    
        usernames_path = os.path.join(os.path.dirname(__file__), "../data/usernames.json")

        if not os.path.exists(usernames_path):
            return None

        with open(usernames_path, "r") as usernames_f:
            names = json.loads(usernames_f.read())["list_usernames"]

        index = steam_id % 2147483647
        index = index % len(names)

        return names[index]
    
    except json.JSONDecodeError:
        return None
    except Exception:
        return None

def request_steam(id64: str):
    clear_screen()
    print(faded + footer)

    url = f"https://steamcommunity.com/profiles/{id64}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            if "Sorry!" in response.text:
                print(f"{Style.BRIGHT+Fore.LIGHTRED_EX}Error ID: {id64}\n{Style.RESET_ALL}")

            else:

                r_name = get_name(int(id64))

                if r_name:
                    print(f"{Style.BRIGHT+Fore.LIGHTYELLOW_EX}-> {Fore.MAGENTA}Posible nombre {Fore.LIGHTCYAN_EX}\"{r_name}\" {Fore.MAGENTA}de streamer mode para {Fore.LIGHTCYAN_EX}\"{id64}\"\n{Style.RESET_ALL}")
                else:
                    print(f"{Style.BRIGHT+Fore.LIGHTYELLOW_EX}-> {Fore.MAGENTA}Sin resultados de nombre de streamer mode para {Fore.LIGHTCYAN_EX}\"{id64}\"\n{Style.RESET_ALL}")

        else:

            print(f"{Style.BRIGHT+Fore.LIGHTRED_EX}Status code: {response.status_code}\n{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{Style.BRIGHT+Fore.LIGHTRED_EX}{e}\n{Style.RESET_ALL}")