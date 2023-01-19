import colorama
from colorama import Style, Back, Fore
import os
import sys
import subprocess
import discord
import tkinter as tk
import turtle as t
import time
import socket
from subprocess import call
import win32
from win32 import win32console

# Please read this following message down there.

##########################################################################################################################################################################################################################
#  Don't know how to code? Please do not touch the codes that are written here. If you know how to code you can easily touch the codes and edit them on your own. BUT! Don't steal the things and put it in your own OS. #
##########################################################################################################################################################################################################################

colorama.init(autoreset=True)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
win32console.SetConsoleTitle("TuraOS")

print("Running TuraOS 1.0.0")
time.sleep(3)
os.system('cls')
time.sleep(1)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Running on the device.")
time.sleep(0.2)
print(f"[{Fore.YELLOW}PROGRESS{Fore.WHITE}] Installing commands from user/bin.")
time.sleep(0.4)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Running on the IP {ip}.")
time.sleep(0.5)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Running on the hostname {hostname}.")
time.sleep(0.9)
print(f"[{Fore.RED}FAIL{Fore.WHITE}] VM disabled by TuraOS.")
time.sleep(0.3)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Done installing commands from user/bin.")
time.sleep(1)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Verifying source files...")
time.sleep(2)
print(f"[{Fore.GREEN}OK{Fore.WHITE}] Verifying commands...")
time.sleep(3)
os.system('cls')
print("Loading TuraOS. Please wait....")
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

os.system('cls')

def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\sign\\sign.py"])

open_py_file()
# TuraOS. CEO - Wernox.