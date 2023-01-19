import os
import subprocess
from subprocess import call
import colorama
from colorama import Style, Back, Fore
import time

colorama.init(autoreset=True)

srt = input(f"Do you want to install the modules first? {Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} ")

if srt == "Y":
    os.system("pip install python-http-client")
    os.system('pip install charset_normalizer')
    os.system("pip install 2captcha-python")
    os.system("pip install beautifulsoup4")
    os.system("pip install pyinstaller")
    os.system("pip install pylibcheck")
    os.system("pip install pyperclip")
    os.system("pip install pyautogui")
    os.system("pip install pypiwin32")
    os.system("pip install packaging")
    os.system("pip install requests")
    os.system("pip install datetime")
    os.system("pip install selenium")
    os.system("pip install keyboard")
    os.system("pip install colorama")
    os.system("pip install urlopen")
    os.system("pip install discord")
    os.system("pip install asyncio")
    os.system("pip install easygui")
    os.system("pip install tasksio")
    os.system("pip install pystyle")
    os.system("pip install PyNaCl")
    os.system("pip install discum")
    os.system("pip install Popen")
    os.system("pip install Cipher")
    os.system("pip install colour")
    os.system("pip install pillow")
    os.system("pip install psutil")
    os.system("pip install login")
    os.system("pip install emoji")
    os.system("pip install httpx")
    os.system("pip install loads")
    os.system("pip install tqdm")
    os.system("pip install pipe")
    os.system("pip install fore")
    os.system("pip install aes")
    os.system("cls")
if srt == "N":
    print("Running....")
    time.sleep(1)
    os.system('cls')
def opener():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\GANG-Nuker\\GANG-Nuker\\GANG.py"])
opener()