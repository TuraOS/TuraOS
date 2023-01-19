import colorama
import os
import sys
import subprocess
import time
from subprocess import call
import requests

version = "1.0.0"
updates = "None"
newupdates = "1.2.5"




response = requests.get('https://turaos.wixsite.com/home/version125')
if response.status_code == 200:
    print(f'TuraOS. Current Version is {version}. Updates: New Version is out: {newupdates} Install at https://turaos.wixsite.com')
else:
    print(f'TuraOS. Current Version is {version}. Updates: {updates}') 
def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()