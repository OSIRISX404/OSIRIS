import socket
import requests
import json
import time
import pyttsx3
from os import system, name

time.sleep(2)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

engin = pyttsx3.init()
engin.say("  this tool is created by OSIRIS")
print("")
print('''
               ▄───▄...OSIRIS
      v1.0.1...█▀█▀█
               █▄█▄█...Url
 Information...─███──▄▄
               ─████▐█─█...Gathering
     Out Put...─████───█
               ─▀▀▀▀▀▀▀...Get Information

''')
print("")
time.sleep(1.5)
try:
    print('')
    engin.say("Ender your target url")
    engin.runAndWait()
    url = input("Ender your target url\> ")
    print('')
    ip = socket.gethostbyname(url)
except:
    print('')
    print("Please ender an valied url")
else:
    print("Conniting...")


req = requests.get(f"https://ipinfo.io/{ip}/json")
data = json.loads(req.text)
print("")
engin.say(" IP ")
engin.runAndWait()
print(f"[*] ip: {data['ip']}\n")

engin.say(" The Hostname ")
engin.runAndWait()
print(f"[*] The Hostname: {data['hostname']}\n")

engin.say(" The Google Map Location ")
engin.runAndWait()
print(f"[*] The Google Map Location: {data['loc']}\n")

engin.say(f" city ")
engin.runAndWait()
print(f"[*] The Sity: {data['city']}\n")

engin.say(f" Region ")
engin.runAndWait()
print(f"[*] The Region: {data['region']}\n")

engin.say(f" Country ")
engin.runAndWait()
print(f"[*] The Country: {data['country']}\n")

engin.say(" Posatl")
engin.runAndWait()
print(f"[*] The Posatl: {data['postal']}\n")

engin.say(" O R G ")
engin.runAndWait()
print(f"[*] The Org: {data['org']}\n")

engin.say(" The Data ")
engin.runAndWait()
print(f"[*] The Data: {data['postal']}\n")

engin.say("  Thim  Zone ")
engin.runAndWait()
print(f"[*] The Thimezone: {data['timezone']}\n")

engin.say( " Readme ")
engin.runAndWait()
print(f"[*] The Readme: {data['readme']}")
