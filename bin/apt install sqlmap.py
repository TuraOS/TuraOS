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

colorama.init('cls')

question = input(f"""The following package will be installed:
sqlmap

Are you sure you want to install sqlmap?
Size: 1 KB
{Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} """)
if question == "Y":
    print("Unpackinging sqlmap.")
    time.sleep(1)
    print('Unpacking man-db..')
    time.sleep(7)
    print("Installing the whole sqlmap package...")
    time.sleep(4)
    print("Done installing.")
    print("Run the command 'sqlmap2' to run sqlmap.")
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

    open_py_file()
if question == "N":
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

    open_py_file()