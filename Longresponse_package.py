import random
from datetime import datetime
import platform
import time
import json
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
def weather():
    # importing library
    import requests
    from bs4 import BeautifulSoup

    # enter city name
    city = "lucknow"

    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]


    return (temp +" "+ sky)

def x():
    time=datetime.now().time()
    return str(time)

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


def os_id():
    system_info = platform.platform()
    return (system_info)
def Sleep():
    print("How many minuites  I have to sleep?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    return "slept peacefully"


