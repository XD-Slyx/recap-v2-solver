import Solve2
import threading
import json
from colorama import Fore
import time
startzeit = None



def recap():
    global startzeit
    startzeit = time.time()
    result = Solve2.ReCaptcha(
        '6LcKKZAjAAAAAN6Rzp8wQU9cwWxi1TIoB9FH_h1E', #site key
        'https://www.instagram.com/accounts/emailsignup/' #website url
    )
    
    json_data = result
    data_dict = json.loads(json_data['data'])
    endzeit = time.time()
    dauer = endzeit - startzeit
    key = data_dict['Solution']
    print(f"{Fore.RESET}{Fore.MAGENTA}[SOLVER]{Fore.WHITE} SOLVED {Fore.BLUE}{key[:25]}**********{Fore.MAGENTA} -> {Fore.RESET} {dauer}sek")
    



def threads():
    threads = []
    
    for i in range(5):
        t = threading.Thread(target=recap)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def hcap():
 
 result = Solve2.HCaptcha(
     '4c672d35-0701-42b2-88c3-78380b0db560', # siteKey
     'https://discord.com/' # URL Website
 )
 print(result)
recap()