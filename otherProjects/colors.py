#!/usr/bin/python3

#Python colors

msg = "PYTHON IS COLOR"

from colorama import *
init()

print(Fore.YELLOW + Style.BRIGHT + "HELLO")
print(Fore.BLUE + "DEVELOPERS")
print(Fore.RED + "PYTHON IS AWESOME")
print(Fore.YELLOW + msg[0:6] + Fore.BLUE + msg[6:9] + Fore.RED + msg[9:15] )
