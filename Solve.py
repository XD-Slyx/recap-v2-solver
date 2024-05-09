# https://discord.gg/HK9gszBDDy
import undetected_chromedriver as webdriver
import os, time, json
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from colorama import init
import random
import string
import threading
import pyperclip
import secrets
import time
from faker import Faker
import httpx
import pyautogui
import time
from threading import Thread
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import random
import re
from typing import Optional

from seleniumwire import webdriver


chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v6986836679788817342 t4937772023959314365 ath1fb31b7a altpriv cvcv=2 smf=0")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=0")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])






startzeit = None
def start():
    global startzeit
    startzeit = time.time()
def end():
    endzeit = time.time()
    dauer = endzeit - startzeit
def RunProfile(type):
    # chrome://version/
    profile = 'C:\\Users\\abdul\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 16'

    chrome_options.add_argument(f'--load-extension={os.path.abspath("recaptcha")}')

    driver = webdriver.Chrome(options=chrome_options)

    driver.minimize_window()
    print(f"{Fore.RESET}{Fore.MAGENTA}[QUASAR-SOLVER]{Fore.WHITE} Started recaptcha v2 Task")
    return driver




    

def ReCaptcha(key, url):
    script = """
    const newBody = document.createElement('body');
    const recaptchaDiv = document.createElement('div');
    recaptchaDiv.classList.add('g-recaptcha');
    recaptchaDiv.dataset.sitekey = '{}';
    const script = document.createElement('script');
    script.src = 'https://www.google.com/recaptcha/api.js';
    newBody.appendChild(recaptchaDiv);
    newBody.appendChild(script);
    document.documentElement.replaceChild(newBody, document.body);
    """.format(key)

    driver = RunProfile('recaptcha')
    driver.get(url)

    while True:
        try:
            res = driver.execute_script("return document.querySelector('.g-recaptcha').dataset['sitekey']")
            if res == key:
                break
        except:
            driver.get(url)
            time.sleep(5)
            driver.execute_script(script)
            time.sleep(3)
    
    while True:
        try:
            user_agent = driver.execute_script("return navigator.userAgent")
            res = driver.execute_script("return document.getElementById('g-recaptcha-response-1').value")
            data = {
                'Solution': res,
                'User-Agent': user_agent
            }
            if res != '':
                driver.quit()
                return {'status': True, 'data': json.dumps(data)}
            else:
                time.sleep(3)
        except:
            time.sleep(3)
            continue

