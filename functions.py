import requests
import subprocess
import time
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup


def accessSite(siteName, match):
    url = siteName
    resp = requests.get(url)
    if resp.status_code == 200:
        print("Reading site")
        soup = BeautifulSoup(resp.text, 'html.parser')
        match = soup.find(match, style="background-color:white;padding:10px; overflow:auto; height:80%")
        str = match.text.replace("\n", "")
        list = str.split(" ")
        print("script gathered")
        return list
    else:
        print("error")


def sendWords(list):
    try:
        subprocess.call(["/usr/bin/open", "/System/Applications/Messages.app"])
        time.sleep(3)
        keyboard = Controller()
        i = 0;
        for word in list:
            i = i + 1
            if i <= 5:
                keyboard.type(word)
        return
    except Exception as e:
        print(str(e))
