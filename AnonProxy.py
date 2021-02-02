
import requests
from colorama import *
import os 
import time
import random

init(convert=True)


os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title AnonProxy ~ Anonymous")
print("テキストファイルを新規作成しています...")
time.sleep(3)
os.system('cls')
print('''
      .o.                                         
     .888.                                        
    .8"888.     ooo. .oo.    .ooooo.  ooo. .oo.   
   .8' `888.    `888P"Y88b  d88' `88b `888P"Y88b  
  .88ooo8888.    888   888  888   888  888   888  
 .8'     `888.   888   888  888   888  888   888  
o88o     o8888o o888o o888o `Y8bod8P' o888o o888o 
                                                  
                                                  
                                                  
ooooooooo.                                              
`888   `Y88.                                            
 888   .d88' oooo d8b  .ooooo.  oooo    ooo oooo    ooo 
 888ooo88P'  `888""8P d88' `88b  `88b..8P'   `88.  .8'  
 888          888     888   888    Y888'      `88..8'   
 888          888     888   888  .o8"'88b      `888'    
o888o        d888b    `Y8bod8P' o88'   888o     .8'     
                                            .o..P'      
                                            `Y8P'       
                                                        

AnonProxyは匿名性の高いProxyのみをスクレイピングします。
GitHub : https://github.com/ERM073
Twitter: https://twitter.com/AnonMusic7
    ''')
# FILES

https_file = open("https.txt","w") 
socks4_file = open("socks4.txt", "w")
http_file = open("http.txt", "w")
socks5_file = open("socks5.txt", "w")


# REQUEST API

rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rs4 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4')
rs5 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5')


# HTTPS

https = []
https = rhttps.text
https = https.split()
lines = len(https)


# HTTP

http = []
http = rhttp.text
http = http.split()
hlines = len(http)


# SOCKS 4

socks4 = []
socks4 = rs4.text
socks4 = socks4.split()
slines = len(socks4)

# SOCKS 5

socks5 = []
socks5 = rs5.text
socks5 = socks5.split()
sslines = len(socks5)


number = random.randint(1, 5)

def getsocks4():
    for i in range(number):
        print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTCYAN_EX + "HTTPS" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + https[number])
        time.sleep(0)




def getsocks5():
    for b in range(number):
        print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTMAGENTA_EX + "SOCKS5" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + socks5[number])
        time.sleep(0)



def main():
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "1" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + "HTTPS")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "2" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + "HTTP")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "3" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + "SOCKS4")
    print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX  + "4" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTRED_EX + "SOCKS5")
    print(Fore.RESET + ' ')
    a = input(Fore.LIGHTWHITE_EX + "Proxyを選択してください: ")
    if(a == "1"):
        for i in range(lines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTCYAN_EX + "HTTPS" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + https[i])
            https_file.write('\n' + https[i])
            time.sleep(0)
    elif(a == "2"):
        for a in range(hlines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTMAGENTA_EX + "HTTP" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + http[a])
            http_file.write('\n' + http[a])
            time.sleep(0)
    elif(a == "3"):
        for b in range(slines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTYELLOW_EX + "SOCKS4" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + socks4[b])
            socks4_file.write('\n' + socks4[b])
            time.sleep(0)
    elif(a == "4"):
        for c in range(sslines):
            print(Fore.LIGHTWHITE_EX + "[ " + Fore.LIGHTRED_EX + "SOCKS5" + Fore.LIGHTWHITE_EX + " ] " + Fore.LIGHTGREEN_EX + socks5[c])
            socks5_file.write('\n' + socks5[c])
            time.sleep(0)

if __name__ == "__main__":
    main()