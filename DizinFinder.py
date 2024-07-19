import requests
import argparse
import threading
from colorama import *
import os
import random
init(autoreset=True)
a = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]
headers = {'User-Agent': random.choice(a)}

def banner():
  text = Fore.RED + '''
   ooooooooo.   ooooo   ooooo       .o.       ooooooooo.     .oooooo.   .oooooo..o
   888   `Y88. `888'   `888'      .888.      `888   `Y88.  d8P'  `Y8b  d8P'    `Y8
   888   .d88'  888     888      .8"888.      888   .d88' 888      888 Y88bo.
   888ooo88P'   888ooooo888     .8' `888.     888ooo88P'  888      888  `"Y8888o.
   888          888     888    .88ooo8888.    888`88b.    888      888      `"Y88b
   888          888     888   .8'     `888.   888  `88b.  `88b    d88' oo     .d8P
  o888o        o888o   o888o o88o     o8888o o888o  o888o  `Y8bood8P'  8""88888P'
  '''
  print(text)
  (Style.RESET_ALL)

def scan(url):
  file = input(Fore.YELLOW + 'Bir dosya yolu giriniz: ')
  w = open(file, 'r')
  banner()
  for dos in w:
    try:
     dosya = dos.strip()
     payload = url + '/' + dosya
     r = requests.get(payload,headers=headers)
     if r.status_code == 200:
      print(Fore.WHITE + '--' * 40)
      print(f'Dizin bulundu ==> {payload}')
      print(Fore.YELLOW + '--' * 40)
    except KeyboardInterrupt:
     print(f"Kullanıcı çıktı")
     exit()

if __name__ == '__main__':
 z = argparse.ArgumentParser()
 z.add_argument('--url', required=True,help="Url")
 args = z.parse_args()
 url = args.url
 main =  threading.Thread(target=scan(url))
 main.start()
