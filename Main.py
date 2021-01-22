#####################################################################
#                                                                   #
#  Dew3's Roblox Username Checker                                   # 
#  v0.2                                                             #
#  Utilizes robloxapi by iranathan                                  #
#                                                                   #
#####################################################################

import robloxapi, asyncio
import requests
import pathlib
import colorama
import os, sys
import time
from pathlib import Path
from colorama import *


client = robloxapi.Client()
current_path = os.path.dirname(os.path.realpath(__file__))
open(current_path +"/"+str("Available")+str("")+".txt","a") #Creates 'Available.txt'
open(current_path +"/"+str("Usernames")+str("")+".txt","a") #Creates 'Usernames.txt'
names = open('Usernames.txt', 'r') 
available = open('Available.txt', 'w') 
mypath = Path('Usernames.txt')
numberOfUsernames = 0


async def check():
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+"Dew3's Roblox Username Checker")

    if mypath.stat().st_size == 0: #If the Usernames files is empty it will prompt the user to enter usernames and close the program
        print(Fore.WHITE+"\nPlease put your names in Usernames.txt"+ Fore.RED + "\nClosing in 5 seconds")
        time.sleep(5)
        sys.exit()
    else:  
            pass
    with open('Usernames.txt', 'r') as u: 
            
            for line in u:
                time.sleep(0)
                username = line.rstrip("\n") #Gets each usernames line in 'Usernames.txt'

                if len(username) > 2 and len(username) < 21: 
                    global numberOfUsernames
                    numberOfUsernames += 1 #Counter for the total number of usernames
                    user = await client.get_user_by_username(username) #robloxapi either returns a user object or None if the user doesn't exist
                    if user == None:
                        time.sleep(0)

                        available.write(username + "\n") #The username isn't taken so we store it into 'Availables.txt'
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"Not Taken"+Fore.WHITE+"]" +Fore.WHITE +username)
                    
                    else:
                        time.sleep(0)
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"Taken"+Fore.WHITE+"]" +Fore.WHITE +username)
            
tic = time.perf_counter() #Program timer start
asyncio.run(check())
toc = time.perf_counter() #Program timer stop
available.close()         
print(Fore.CYAN+"\nChecker finished " + str(numberOfUsernames) + f" usernames in {toc - tic:0.4f} seconds")
print("Saved " + str(savedNames) + " usernames saved!")
print(Fore.RED +"Closing in 5 seconds")
time.sleep(5)
sys.exit()

