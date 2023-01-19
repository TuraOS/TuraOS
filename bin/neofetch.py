import subprocess
from subprocess import call
import colorama
from colorama import Style, Fore, Back
import socket
import sys
import time
import os
import multiprocessing


colorama.init(autoreset=True)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
cores = multiprocessing.cpu_count()

print(f"""
 ___                 ___  ___    ___                   _            _ 
|_ _| _ _  _ _  ___ | . |/ __]  |_ _| ___  _ _  _ _ _ [_] _ _  ___ | |
 | | | | || '_][_] || | |\__ \   | | / ._]| '_]| ' ' || || ' |[_] || |
 |_|  \__||_|  [___|`___'[___/   |_| \___.|_|  |_|_|_||_||_|_|[___||_|
                                                                      

IP: {ip}
Hostname: {hostname}
Cores: {cores}












""")
def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()