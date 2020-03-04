import requests
import re
from bs4 import BeautifulSoup

url = 'https://weather.com/ru-RU/weather/today/l/RSXX0063:1:RS'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return r.text            

def get_temperature(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-temp')
    temperature = re.findall(r'\d{1,2}', str(buffer[0]))
    return temperature[0]

def get_weather(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-phrase')
    weather = re.findall(r'[А-Я,а-я]', str(buffer[0]))
    return ''.join(weather)

def get_speed(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-sidecar component panel')
    speed = re.findall(r'\d{1,2}', str(buffer[0]))
    return speed[0]

def get_date(temp, wether, speed):
    return "Погода в Москве сейчас:\n" + str(temp) + "°, " + str(wether) + "\nВетер " + str(round(float(speed)/3.6, 2)) + " м/с"

def weather():
    page = get_html(url)
    html = BeautifulSoup(page, 'lxml')
    return get_date(get_temperature(html), get_weather(html), get_speed(html))