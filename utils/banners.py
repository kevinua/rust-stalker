import fade
from colorama import Fore, Style

ascii = f"""
           ___    _ ____
          |_ _|__| / ___|  ___ __ _ _ __  _ __   ___ _ __
           | |/ _` \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
           | | (_| |___) | (_| (_| | | | | | | |  __/ |
          |___\__,_|____/ \___\__,_|_| |_|_| |_|\___|_|
"""
faded = fade.purpleblue(ascii)

footer = f"""\n{Style.BRIGHT+Fore.GREEN}     Herramienta creada por EvolNet con fines streamsnipers.\n{Style.RESET_ALL}"""