import ipdata
from ipdata import ipdata
import subprocess
from subprocess import call
    

apikey = "7f32279ab303d2b474c05c4d07fdd892f4156d6e45b5d630c2fa5c98"

ip = input("IP: ")  
    
ipd = ipdata.IPData(apikey)
response = ipd.lookup(ip)
print(response)
def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()