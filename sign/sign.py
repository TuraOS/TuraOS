import maskpass
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
import stdiomask
from stdiomask import getpass
import hashlib
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import threading
from tqdm.tk import tqdm
from time import sleep
clear = lambda: os.system('cls')

colorama.init(autoreset=True)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

window = Tk()    

pbar = tqdm(total=30, tk_parent=window)    


for _ in range(30):
    sleep(0.1)
    pbar.update(1)
    pbar.close() 
    

    
window.mainloop()



print("Running TuraOS 1.5.0")
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



def signup():
    email = input("User > ")
     
    pwd = maskpass.askpass(prompt="Password >", mask="*")
    conf_pwd = maskpass.askpass(prompt=" Confirm Password >", mask="*")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("User_Data.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
        time.sleep(2)
        os.system('cls')
    else:
        print("Password is not same as above! \n")
def login():
    user = input("User > ")
    pwd = input("Password > ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("User_Data.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if user == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         time.sleep(2)
         os.system('cls')
    else:
         print("Login failed! \n")
         time.sleep(2)
         os.system('cls')
print("********** Login System **********")
print("[1] Sign up")
print("[2] Login")
print("[3] Exit")
ch = int(input("> "))
if ch == 1:
    signup()
elif ch == 2:
    login()
elif ch == 3:
    quit()
else:
    print("Wrong Choice!")



print("Welcome! Please wait while we load TuraOS.")
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
time.sleep(2)
os.system('cls')

def open():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])
open()
