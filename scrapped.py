import argparse
import requests, bs4

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
    prog='Scrapped',
    description='''
    A Python Website Scrapper tool.
    ''',
    epilog='Copyright (c) ©2021 NexuZDragon'
    )

defaultIs = 'Use -h Parameter to show Help.'

parser.add_argument('-u', '--url', default='Use -h Parameter to show Help.', help="Set target url.")
parser.add_argument('-sT', '--scrap_tag', default=defaultIs, help='Scrap Code.      Methods = P, H1, A.')
parser.add_argument('-m', '--method', default='Use -h Parameter to show Help', help='[P, Methods = FULL_TEXT, ID, CLASS] [H1-H6, Methods = NO METHOD] [A, Methods = HREF, CLASS]')
parser.add_argument('-i', '--info', default='Use -h Parameter to show Help', help='Informations = ROBOTS.TXT')
parser.add_argument('-sH', '--show_help', default='Use -h Parameter to show Help', help='Show Help of a Parameter ex: -sH P')

WColor = '\u001b[0m'
LYColor = '\u001b[33;1m'
LBColor = '\u001b[34;1m'
LRColor = '\u001b[31;1m'
LGColor = '\u001b[32;1m'
LCColor = '\u001b[36;1m'

startLayer = '''
            -- + [-- Scrapped --] + --
                  Scrap For Free
                  
'''

args = parser.parse_args()
getUsrIP = requests.get("https://api64.ipify.org").text

if args.url != 'Use -h Parameter to show Help.':
    print(startLayer)
    getTarget = requests.get(args.url)
    with open('data/target.html', 'w') as f:
        f.write(str(getTarget.content))
    
    extractUrl = args.url.replace("https://", "").replace("/", "").replace("http://", "")
    
    print(f' Request [+] {getUsrIP} > {extractUrl}')
    
    with open('data/target.html') as THandler:
        targetHandler = BeautifulSoup(THandler, 'lxml')
    
    if getTarget.status_code == 404 or getTarget.status_code == 403:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        
    else:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        print()
        
        if args.scrap_tag == "P":
            pTags = []
            
            if args.method == 'FULL_TEXT':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.text)
            
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif args.method == 'ID':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.get('id'))
                
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif args.method == 'CLASS':
                for tags in targetHandler.find_all('p'):
                    pTags.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(pTags)
                for tags in pTags:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif args.method != defaultIs:
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
            
        elif args.scrap_tag == 'H1':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'H2':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'H3':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'H4':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'H5':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'H6':
            h1Storage = []
            
            if args.method == defaultIs:
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
            
        elif args.scrap_tag == 'A':
            aStorage = []
            
            if args.method == 'HREF':
                for tags in targetHandler.find_all('a'):
                    aStorage.append(tags.get('href'))
                
                setVal = 1
                GetLenFromArray = len(aStorage)
                for tags in aStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
                
            elif args.method == 'CLASS':
                for tags in targetHandler.find_all('a'):
                    aStorage.append(tags.get('class'))
                
                setVal = 1
                GetLenFromArray = len(aStorage)
                for tags in aStorage:
                    print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                    setVal += 1
                setVal = 0
            
            elif args.method != defaultIs:
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
            
        elif args.scrap_tag != defaultIs:
            pass
        
        if args.info == 'ROBOTS.TXT':
            disallowedR = []
            
            getRobots = requests.get(f'https://{extractUrl}/robots.txt')
            with open('data/robots.html', 'w') as savRob:
                savRob.write(str(getRobots.content))
            
            with open('data/robots.html') as savFile:
                robotsHandler = BeautifulSoup(savFile, 'lxml')
                
            
            for disallows in robotsHandler.find_all('Disallow:'):
                disallowedR.append(disallows.get('Disallow:'))
            
            print(getRobots.text.replace("Disallow: ", f'{WColor}[{LRColor}DISALLOWED{WColor}] ').replace('Allow: ', f'{WColor}[{LGColor}ALLOWED{WColor}] ').replace('Sitemap: ', f'{WColor}[{LCColor}SITEMAP{WColor}] ').replace('User-agent: ', f'{WColor}[{LBColor}USER-AGENT{WColor}] ').replace('# ', f'{WColor}[{LGColor}TAG{WColor}] '))
            
        elif args.info == 'DNSLOOKUP':
            getDns = requests.get(f'https://api.hackertarget.com/dnslookup/?q={extractUrl}')
            print(getDns)
    
else:
    print("to Show more Help Use -h")

if args.show_help == 'P':
    print('Methods = FULL_TEXT, ID, CLASS')
    print('- To Use = -sT P')
    print('- With Method = -sT P -m FULL_TEXT')
    print()
    print('To Use with Full Params')
    print('-$ python3 scrapped.py -u https://ex.com -sT P -m FULL_TEXT')
    

elif args.show_help == 'A':
    print('Methods = HREF, CLASS')
    print('- To Use = -sT A')
    print('- With Method = -sT A -m HREF')
    print()
    print('To Use with Full Params')
    print('-$ python3 scrapped.py -u https://ex.com -sT A -m HREF')