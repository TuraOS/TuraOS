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
import ipdata
from ipdata import ipdata

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"Your IP is: {ip}")
def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()