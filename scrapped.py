import argparse
import requests, bs4
import os, platform
import subprocess
import time

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
    prog='Scrapped',
    description='''
    A Python Website Scrapper tool.
    ''',
    epilog='Copyright (c) 2021 tryn4hek'
    )

defaultIs = 'Use -h Argument to show Help.'

parser.add_argument('-u', '--url', default='Use -h Argument to show Help.', help="Set target url.") # URL

parser.add_argument('-sT', '--scrap_tag', default=defaultIs, help='Scrap Code.      Methods = P, H1, A, IMG, LINK, INPUT, BUTTON') # SCRAP TAG

parser.add_argument('-m', '--method', default='Use -h Argument to show Help', help='[P, Methods = FULL_TEXT, ID, CLASS] [H1-H6, Methods = NO METHOD] [A, Methods = HREF, CLASS] [IMG, Methods = SRC, ALT, CLASS') # METHOD

parser.add_argument('-i', '--info', default='Use -h Argument to show Help', help='Informations = ROBOTS.TXT, DNSLOOKUP, PORTSCAN.') # INFO

parser.add_argument('-sH', '--show_help', default='Use -h Argument to show Help', help='Show Help of a Argument ex: -sH P/-sH SCRAP_TAG') # SHOW HELP

WColor = '\u001b[0m'
LYColor = '\u001b[33;1m'
LBColor = '\u001b[34;1m'
LRColor = '\u001b[31;1m'
LGColor = '\u001b[32;1m'
LCColor = '\u001b[36;1m'

startLayer = f'''
                       Scrap With{LBColor}
    ___   ___  ____    __    ____  ____  ____  ____  
   / __) / __)(  _ \  /__\  (  _ \(  _ \( ___)(  _ \ 
   \__ \( (__  )   / /(__)\  )___/ )___/ )__)  )(_) )
   (___/ \___)(_)\_)(__)(__)(__)  (__)  (____)(____/ 
               {WColor}-- + [-- Scrapped --] + --
                     Scrap For Free
                  
'''

args = parser.parse_args()
getUsrIP = requests.get("https://api64.ipify.org").text

# GetPlatform
getUsrPlatform = platform.system()
if getUsrPlatform == 'Windows':
    print('Platform Not Supported!')
    exit()

argsScrapTag = args.scrap_tag.upper()
argsMethod = args.method.upper()

if args.url != 'Use -h Argument to show Help.':
    print(startLayer)
    getTarget = requests.get(args.url)
    
    with open('data/target.html', 'w') as f:
            f.write(str(getTarget.content))
    extractUrl = args.url.replace("https://", "").replace("http://", "")
    
    print(f' Request [+] {getUsrIP} > {extractUrl}')
    
    with open('data/target.html') as THandler:
        targetHandler = BeautifulSoup(THandler, 'html.parser')
    
    if getTarget.status_code == 404 or getTarget.status_code == 403:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        
    else:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        print()
        
        # --------------- P TAGS ---------------
        if argsScrapTag == "P":
            pTags = []
            
            if argsMethod == 'FULL_TEXT':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.text)
            
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'ID':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.get('id'))
                
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'CLASS':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod != defaultIs:
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags)
                
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            print()
            print(f'=!= Scrapped Website, Total Items: {len(pTags)}')
            print()
            
        # --------------- H TAGS ---------------
        elif argsScrapTag == 'H1':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h1'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        elif argsScrapTag == 'H2':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h2'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        elif argsScrapTag == 'H3':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h3'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        elif argsScrapTag == 'H4':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h4'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        elif argsScrapTag == 'H5':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h5'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        elif argsScrapTag == 'H6':
            h1Storage = []
            
            if argsMethod == defaultIs:
                for tags in targetHandler.find_all('h6'):
                    h1Storage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(h1Storage)
                for tags in h1Storage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(h1Storage)}')
            print()
            
        # --------------- A TAGS ---------------
        elif argsScrapTag == 'A':
            aStorage = []
            
            if argsMethod == 'HREF':
                for tags in targetHandler.find_all('a'):
                    aStorage.append(tags.get('href'))
                
                setVal = 1
                GetLenFromArray = len(aStorage)
                for tags in aStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'CLASS':
                for tags in targetHandler.find_all('a'):
                    aStorage.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(aStorage)
                for tags in aStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod != defaultIs:
                for tags in targetHandler.find_all('a'):
                    aStorage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(aStorage)
                for tags in aStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(aStorage)}')
            print()
            
        # --------------- IMG TAGS ---------------
        elif argsScrapTag == 'IMG':
            imgStorage = []
            
            if argsMethod == 'SRC':
                for tags in targetHandler.find_all('img'):
                    imgStorage.append(tags.get('src'))
                
                setVal = 1
                GetLenFromArray = len(imgStorage)
                for tags in imgStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'ALT':
                for tags in targetHandler.find_all('img'):
                    imgStorage.append(tags.get('alt'))
                
                setVal = 1
                GetLenFromArray = len(imgStorage)
                for tags in imgStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'CLASS':
                for tags in targetHandler.find_all('img'):
                    imgStorage.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(imgStorage)
                for tags in imgStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod != defaultIs:
                for tags in targetHandler.find_all('img'):
                    imgStorage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(imgStorage)
                for tags in imgStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(imgStorage)}')
            print()
        
        # --------------- LINK TAG ---------------
        elif argsScrapTag == 'LINK':
            linkStorage = []
            
            if argsMethod == 'CLASS':
                for tags in targetHandler.find_all('link'):
                    linkStorage.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(linkStorage)
                for tags in linkStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'HREF':
                for tags in targetHandler.find_all('link'):
                    linkStorage.append(tags.get('href'))
                
                setVal = 1
                GetLenFromArray = len(linkStorage)
                for tags in linkStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'REL':
                for tags in targetHandler.find_all('link'):
                    linkStorage.append(tags.get('rel'))
                
                setVal = 1
                GetLenFromArray = len(linkStorage)
                for tags in linkStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'TYPE':
                for tags in targetHandler.find_all('link'):
                    linkStorage.append(tags.get('type'))
                
                setVal = 1
                GetLenFromArray = len(linkStorage)
                for tags in linkStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod != defaultIs:
                for tags in targetHandler.find_all('link'):
                    linkStorage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(linkStorage)
                for tags in linkStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            print()
            print(f'=!= Scrapped Website, Total Items: {len(linkStorage)}')
            print()
        
        # --------------- INPUT TAGS ---------------
        elif argsScrapTag == 'INPUT':
            inputStorage = []
            
            if argsMethod == 'ADDRESS':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('address'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'AUTOCOMPLETE':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('autocomplete'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'CLASS':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'ID':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('id'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'NAME':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('name'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod != defaultIs:
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags)
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif argsMethod == 'TYPE':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('type'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif argsMethod == 'VALUE':
                for tags in targetHandler.find_all('input'):
                    inputStorage.append(tags.get('value'))
                
                setVal = 1
                GetLenFromArray = len(inputStorage)
                for tags in inputStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
        # --------------- BUTTON TAGS ---------------
        elif argsScrapTag == 'BUTTON':
            buttonTags = []
            
            for tags in targetHandler.find_all('button'):
                if argsMethod == 'ARIA-LABEL':
                    buttonTags.append(tags.get('aria-label'))
                    
                elif argsMethod == 'CLASS':
                    buttonTags.append(tags.get('class'))
                    
                elif argsMethod == 'TYPE':
                    buttonTags.append(tags.get('type'))
                    
                elif argsMethod != defaultIs:
                    buttonTags.append(tags)
            
            setVal = 1
            GetLenFromArray = len(buttonTags)
            for tags in buttonTags:
                print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                setVal += 1
            setVal = 0
            
        elif argsScrapTag != defaultIs:
            print(f"{WColor}[{LBColor}•{WColor}] FULL CODE:\n {targetHandler.prettify()}")
        
        # --------------- ROBOTS.TXT INFO ---------------
        if args.info == 'ROBOTS.TXT':
            disallowedR = []
            
            getRobots = requests.get(f'https://{extractUrl}/robots.txt')
            with open('data/robots.html', 'w') as savRob:
                savRob.write(str(getRobots.content))
            
            with open('data/robots.html') as savFile:
                robotsHandler = BeautifulSoup(savFile, 'html.parser')
                
            
            for disallows in robotsHandler.find_all('Disallow:'):
                disallowedR.append(disallows.get('Disallow:'))
            
            print(getRobots.text.replace("Disallow: ", f'{WColor}[{LRColor}DISALLOWED{WColor}] ').replace('Allow: ', f'{WColor}[{LGColor}ALLOWED{WColor}] ').replace('Sitemap: ', f'{WColor}[{LCColor}SITEMAP{WColor}] ').replace('User-agent: ', f'{WColor}[{LBColor}USER-AGENT{WColor}] ').replace('# ', f'{WColor}[{LGColor}TAG{WColor}] '))
            
        # --------------- DNSLOOKUP INFO ---------------
        elif args.info == 'DNSLOOKUP':
            verifyUrl = requests.get(f'https://{extractUrl}').status_code
            if verifyUrl != 200:
                print(f"{WColor}[{LRColor}FAILED{WColor}] : Cannot get DNS From the URL.")
            else:
                getDns = requests.get(f'https://api.hackertarget.com/dnslookup/?q={extractUrl}')
                if getDns != "error input invalid - enter IP or Hostname":
                    print(getDns.text.replace('SOA :', f'{WColor}[{LRColor}SOA{WColor}] :').replace('A :', f'{WColor}[{LGColor}A{WColor}] :').replace('MX :', f'{WColor}[{LYColor}MX{WColor}] :').replace('NS :', f'{WColor}[{LCColor}NS{WColor}] :').replace('TXT :', f'{WColor}[{LBColor}TXT{WColor}] :'))
                    
                else:
                    print(f"{WColor}[{LRColor}FAILED{WColor}] : Invalid Domain, Please enter URL That only contain Domain in it, [ex: https://example.com]")
            print()
            
        # --------------- PORTSCAN INFO ---------------
        elif args.info == 'PORTSCAN':
            getPlatform = platform.machine()
            if getPlatform == 'aarch64':
                verifyRequiredPackage = os.path.exists('/data/data/com.termux/files/usr/bin/nmap')
                verifyRequiredPackage2 = os.path.exists('/usr/bin/nmap')
                if verifyRequiredPackage == True or verifyRequiredPackage2 == True:
                    os.system(f'nmap -p1-200 {extractUrl}')
                    
                elif verifyRequiredPackage == False or verifyRequiredPackage2 == False:
                    print(f'{WColor}[{LRColor}ERROR{WColor}] You dont have Required Package.')
                    verifyUserInstall = input(f'{WColor}[{LRColor}ERROR{WColor}] Do you want to install the Required Package [y/n]? ').lower()
                    
                    if verifyUserInstall == 'y':
                        print(f'{WColor}[{LGColor}+{WColor}] STARTING INSTALLATION.')
                        os.system('apt install nmap -y')
                        
                    elif verifyUserInstall == 'n':
                        exit()
                        
                    
            else:
                verifyRequiredPackage = os.path.exists('/usr/bin/nmap')
                if verifyRequiredPackage == True:
                    os.system(f'nmap -p1-200 -Pn {extractUrl}')
                    
                elif verifyRequiredPackage == False:
                    print(f'{WColor}[{LRColor}ERROR{WColor}] You dont have Required Package.')
                    verifyUserInstall = input(f'{WColor}[{LRColor}ERROR{WColor}] Do you want to install the Required Package [y/N]? ').lower()
                    
                    if verifyUserInstall == 'y':
                        print(f'{WColor}[{LGColor}+{WColor}] STARTING INSTALLATION.')
                        os.system('sudo apt install nmap -y')
                        
                    elif verifyUserInstall == 'n':
                        exit()
    
else:
    print()
    print("to Show more Help Use -h")
    print()

# --------------- SHOW HELP ---------------
if args.show_help == 'P':
    print('Methods = FULL_TEXT, ID, CLASS')
    print('- Example Usage = -sT P')
    print('- With Method = -sT P -m FULL_TEXT')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://ex.com -sT P -m FULL_TEXT')
    print()

elif args.show_help == 'A':
    print('Methods = HREF, CLASS')
    print('- Example Usage = -sT A')
    print('- With Method = -sT A -m HREF')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://ex.com -sT A -m HREF')
    print()

elif args.show_help == 'IMG':
    print('Methods = SRC, ALT, CLASS')
    print('- Example Usage = -sT IMG')
    print('- With Method = -sT IMG -m SRC')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://example.com -sT IMG -m SRC')
    print()
    

elif args.show_help == 'INPUT':
    print('Methods = ADDRESS, AUTOCOMPLETE, CLASS, ID, NAME, TYPE, VALUE')
    print('- Example Usage = -sT INPUT')
    print('- With Method = -sT INPUT -m (method)')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u (url) -sT INPUT -m (method)')

elif args.show_help == 'LINK':
    print('Methods = CLASS, HREF, REL, TYPE')
    print('- Example Usage = -sT LINK')
    print('- With Method = -sT LINK -m (method)')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://example.com -sT LINK -m (METHOD)')
    print()

elif args.show_help == 'BUTTON':
    print('Methods = CLASS, TYPE, ARIA-LABEL')
    print('- Example Usage ° -sT BUTTON')
    print('- With Method = -sT BUTTON -m (method)')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u (url) -sT BUTTON -m (method)')

elif args.show_help == 'info':
    print('Available Info: ROBOTS.TXT, DNSLOOKUP')
    print('- Example Usage = -i ROBOTS.TXT, PORTSCAN')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://example.com -i ROBOTS.TXT')
    print()

elif args.show_help == 'SCRAP_TAG':
    print('Available Tags: P, A, H1-H6, IMG, LINK, INPUT, BUTTON.')
    print()
    print('Full Usage')
    print('-$ python3 scrapped.py -u https://example.com -sT (tag)')
    print()