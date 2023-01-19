import subprocess
from subprocess import call
import time

echo = input("Message: ")

print(echo)


def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()