from pypresence import Presence
import time 


id = input("ID Of your Bot: ")
title = input("State of the Presence:")
thing = input("Details of the Presence: ")
ae = input("Large Text: ")
again = input("Details of the Presence again: ")
moment = input("State of the presence again: ")
print("All set!")
time.sleep(1)
rpc = Presence(id)
rpc.connect()
print("Presence is running.")

rpc.update(state=title,details=thing)

while True:
    rpc.update(
        large_text=ae,
        details=again,
        state=moment
    )