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

colorama.init(autoreset=True)


question = input(f"Are you sure you want to exit the terminal? {Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE} ")
if question == "Y":
    print("Exiting....")
    time.sleep(0.8)
    quit()
if question == "N":
    def open_py_file():
      call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

    open_py_file()