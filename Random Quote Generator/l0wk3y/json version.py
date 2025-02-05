import json
import os
import random
from time import sleep

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
    
os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open('quotes.json', 'r') as file:
        quotes = json.load(file)

        while True:
            quote = random.choice(quotes)
            print(f"\r{quote['q']} - {bcolors.OKGREEN}{quote['a']}{bcolors.ENDC}", end='', flush=True)
            sleep(5)
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n\n{bcolors.OKGREEN}Goodbye!{bcolors.ENDC}')
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')