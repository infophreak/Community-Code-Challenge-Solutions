import requests
import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

response = requests.get('https://zenquotes.io/api/quotes')
author = response.json()[0]['a']
quote = response.json()[0]['q']

while True:

    response = requests.get('https://zenquotes.io/api/quotes')
    author = response.json()[0]['a']
    quote = response.json()[0]['q']
    print(f'{quote} - {author}')
    sleep(3)

