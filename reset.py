import os
import pathlib
import shutil
import psutil
from colorama import init, Fore, Back, Style
from datetime import datetime

version = "1.0"
init()

def title():
    print(Fore.RED + """
██████╗ ███████╗███████╗███████╗████████╗██████╗ ███████╗███████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝
██████╔╝█████╗  ███████╗█████╗     ██║   ██║  ██║█████╗  ███████╗█████╔╝ 
██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║   ██║  ██║██╔══╝  ╚════██║██╔═██╗ 
██║  ██║███████╗███████║███████╗   ██║   ██████╔╝███████╗███████║██║  ██╗
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝""")
    print(Fore.RED   + "———————————————————————————————————————————————————————————")
    print(Fore.WHITE    + "a tool to reset AnyDesk ID")
    print(Fore.RED   + "———————————————————————————————————————————————————————————")
    print(Fore.WHITE    + f"build {version} - by hendyanwilly (github.com/hendyanwilly)")
    print(Fore.WHITE    + f"donate with saweria: " + Fore.YELLOW + "saweria.co/hendyanwilly")
    print(Fore.RED   + "———————————————————————————————————————————————————————————")

def log(text, end = "\n"):
    print(Fore.GREEN + "[" + str(datetime.now()) + "] " + Fore.WHITE + text + Fore.RESET, end = end)

title()
appdata_folder = os.getenv('APPDATA')

file_path = os.path.join(appdata_folder, 'AnyDesk', 'service.conf')
file_path2 = r'C:\ProgramData\AnyDesk\service.conf'

if os.path.isfile(file_path):
    log("Found a portable version of AnyDesk!")

if os.path.isfile(file_path2):
    log("Found a installed version of AnyDesk!")

if os.path.isfile(file_path) == False and os.path.isfile(file_path2) == False:
    log("There is no AnyDesk in this device or ID has been reset!")
    log("Press enter to exit...", end="")
    input()
    quit()
else:
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'AnyDesk.exe':
            log("Terminating AnyDesk process...")
            process.kill()

    try:
        if os.path.isfile(file_path):
            log("Resetting AnyDesk (Portable Version) ID...")
            os.remove(file_path)
            log("AnyDesk (Portable Version) ID has been reset!")
    except:
        print(f"Failed to reset AnyDesk (Portable Version) ID!")

    try:
        if os.path.isfile(file_path2):
            log("Resetting AnyDesk (Installed Version) ID...")
            os.remove(file_path2)
            log("AnyDesk (Installed Version) ID has been reset!")
    except:
        print(f"Failed to reset AnyDesk (Installed Version) ID!")

    log("Press enter to exit...", end="")
    input()
    quit