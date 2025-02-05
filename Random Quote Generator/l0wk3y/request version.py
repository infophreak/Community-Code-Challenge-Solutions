import requests
import os
import random
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    while True:
        response = requests.get('https://raw.githubusercontent.com/infophreak/Community-Code-Challenge-Solutions/refs/heads/main/Random%20Quote%20Generator/l0wk3y/quotes.json')
        quotes = response.json()
        quote = random.choice(quotes)
        print(f"\r{' ' * 80}", end='', flush=True)
        print(f"\r{quote['q']} - {bcolors.OKGREEN}{quote['a']}{bcolors.ENDC}", end='', flush=True)
        sleep(3)
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n\n{bcolors.OKGREEN}Goodbye!{bcolors.ENDC}')
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
