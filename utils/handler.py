import signal, sys, os, requests, json
from utils.banners import *

USERNAMES_PATH = os.path.join(os.path.dirname(__file__), "../data/usernames.json")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    clear_screen()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def load_usernames():
    try:
        if not os.path.exists(USERNAMES_PATH):
            return None

        with open(os.path.join(USERNAMES_PATH), "r") as usernames_f:
            return json.load(usernames_f).get("list_usernames", [])

    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return None

usernames = load_usernames()

def get_name(steam_id: int):
    if not usernames:
        return None

    index = steam_id % 2147483647 % len(usernames)
    return usernames[index]

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
