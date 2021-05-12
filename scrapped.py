import argparse
import requests, bs4

from bs4 import BeautifulSoup

parser = argparse.ArgumentPareser(
    prog='Scrapped',
    description='''
    A Python Website Scrapper tool.
    ''',
    epilog='Copyright (c) ©2021 NexuZDragon'
    )

defaultIs = 'Use -h Parameter to show Help.'

parser.add_argument('-u', '--url', default='Use -h Parameter to show Help.', help="Set target url.")
parser.add_argument('-sT', '--scrap-Tag', default=defaultIs, help='Scrap Code.\n      P   = Scrap P Tags.\n      H1  = Scrap H1 Tags.')

WColor = '\u001b[0m'
LYColor = '\u001b[33;1m'
LBColor = '\u001b[34;1m'

args = parser.parse_args()
getUsrIP = requests.get("https://api64.ipify.org").text

if args.url != 'Use -h Parameter to show Help.':
    getTarget = requests.get(args.url)
    with open('data/target.py', 'w') as f:
        f.write(getTarget.content)
    
    extractUrl = args.url.replace("https://", "").replace("/", "").replace("http://", "")
    
    print(f' Request [+] {getUsrIP} > {extractUrl}')
    
    with open('data/target.py') as THandler:
        targetHandler = BeautifulSoup(THandler, 'lxml')
    
    if getTarget.status_code == 404 || getTarget.status_code == 403:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        
    else:
        print(f' Receive [+] {getUsrIP} < {extractUrl}, Code: {getTarget.status_code}')
        
        
        if args.sT == "P":
            pTags = []
            
            for tags in targetHandler.find_all('p'):
                pTags.append(tags)
            
            setVal = 1
            GetLenFromArray = len(pTags)
            for tags in pTags:
                print(f"{WColor}-$ {LYColor}({WColor}{setVal}{LYColor}/{WColor}{GetLenFromArray}{LYColor}) {LBColor}[+]{WColor} {tags}")
                setVal += 1
    
else:
    pass