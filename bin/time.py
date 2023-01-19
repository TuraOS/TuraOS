from datetime import date
import subprocess
from subprocess import call

todays_date = date.today()

print("Today's date is:", todays_date)
def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])
open_py_file()