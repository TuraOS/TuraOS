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
import webbrowser

colorama.init(autoreset=True)

startup = input(f"""
  (    ( .  (   (   (    ((.  (   ((   
  )\  ()) . )\  )\  )\   ))\. )\  ))\  
 ((_)((_)) ((_)((_)((_)(((_) ((_)((_)))
/ __|/ __|/ _ \| _ \ _ \_ _|/ _ \| \| |
\__ \ (__| (_) |   /  _/| || (_) | .  |
|___/\___|\___/|_|_\_| |___|\___/|_|\_|


____________________________________________________________________

{Fore.RED}Welcome to the Elite Scorpion Hacker Tool. Made by Wernox.

{Fore.WHITE}Select the Following Choice.

[1] Text Spammer
[2] Link Spammer
[3] IP Look Up
[4] Open Exploit Database Website
[5] Quit

> """)
if startup == "1":
    import colorama
    from colorama import Back, Fore, Style

    colorama.init(autoreset=True)

    print(Fore.RED + """
    Loading Text Spammer....
    """)
    time.sleep(3)
    message = input("Spam Message: ")

    input("Please select a thing where you type messages, when ready hit 'ENTER'.")




    import pyautogui,time
    time.sleep(5)
    for i in range(170):
      pyautogui.write(message)
      pyautogui.press("enter")
      print("Sented message.")
if startup == "2":
    import colorama
    from colorama import Back, Fore, Style

    colorama.init(autoreset=True)

    print(Fore.RED + """
    Loading Link Spammer....
    """)
    time.sleep(3)
    message = input("Link Message: ")

    input("Please select a thing where you type messages, when ready hit 'ENTER'.")




    import pyautogui,time
    time.sleep(5)
    for i in range(1):
      pyautogui.write(message)
      pyautogui.press("enter")
      print("Sented message.")
if startup == "3":
    import ipdata
    from ipdata import ipdata
    apikey = "7f32279ab303d2b474c05c4d07fdd892f4156d6e45b5d630c2fa5c98"

    ip = input("IP: ")  
    
    ipd = ipdata.IPData(apikey)
    response = ipd.lookup(ip)
    print(response)
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\scorpion.py"])

    open_py_file()
if startup == "4":
    webbrowser.open('https://www.exploit-db.com/')
    os.system('cls')
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\scorpion.py"])

    open_py_file()

if startup == "5":
    message = input(f"Are you sure you want to quit? {Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} ")
    if message == "Y":
      def open_py_file():
        call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

    open_py_file()
    if message == "N":
        os.system('cls')
        def open_py_file():
          call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\bin\\scorpion.py"])

        open_py_file()