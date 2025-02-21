import re
from utils.banners import *
from utils.handler import *
from colorama import Fore, Style

def main():
    while True:
        clear_screen()
        print(faded + footer)

        id64 = input(f"{Style.BRIGHT+Fore.LIGHTRED_EX}-> {Style.RESET_ALL}")

        if re.match(r'^\d{17}$', id64):
            request_steam(id64)
            break

if __name__ == "__main__":
    main()