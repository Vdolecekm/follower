from platforms import get_ig_acc, get_tt_acc, get_yt_acc
from colorama import Fore, Style, init
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import sys

init(autoreset=True)

print(Fore.BLUE + r"""
  _____    ___    _       _        ___   __        __  _____   ____  
 |  ___|  / _ \  | |     | |      / _ \  \ \      / / | ____| |  _ \ 
 | |_    | | | | | |     | |     | | | |  \ \ /\ / /  |  _|   | |_) |
 |  _|   | |_| | | |___  | |___  | |_| |   \ V  V /   | |___  |  _ < 
 |_|      \___/  |_____| |_____|  \___/     \_/\_/    |_____| |_| \_ 
""")

print(Fore.BLUE + "═════════════════════════════════════\nAuthor: https://github.com/Vdolecekm \nVersion: 1.0.0 \n═════════════════════════════════════")

if __name__ == "__main__":
    username = sys.argv[1]

    try:
        x = get_ig_acc(username)
        print((Fore.GREEN if "https://instagram.com" in x else Fore.RED) + x)
    except PlaywrightTimeoutError:
        print(Fore.YELLOW + "[-] Instagram request timed out!")

    try:
        x = get_yt_acc(username)
        print((Fore.GREEN if "https://www.youtube.com" in x else Fore.RED) + x)
    except PlaywrightTimeoutError:
        print(Fore.YELLOW + "[-] Youtube request timed out!")

    try:
        x = get_tt_acc(username)
        print((Fore.GREEN if "https://www.tiktok.com" in x else Fore.RED) + x)
    except PlaywrightTimeoutError:
        print(Fore.YELLOW + "[-] TikTok request timed out!")