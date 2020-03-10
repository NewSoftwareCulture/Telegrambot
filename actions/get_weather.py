import requests
import re
from bs4 import BeautifulSoup

url_moskow = 'https://weather.com/ru-RU/weather/today/l/34f2aafc84cff75ae0b014754856ea5e7f8ddf618cf9735549dfb5e016c28e10'
url_istra = 'https://weather.com/ru-RU/weather/today/l/9eb64ebb0b188368bfd85f2f21287b6414b49868940baa954cc82970817b77f9'
url_tlt = 'https://weather.com/ru-RU/weather/today/l/d3d7d67737fa39fe26c8dfc95f4ab93e28993b68f320492bbad7a4f2eb7d958d'
url_spb = 'https://weather.com/ru-RU/weather/today/l/4edb4827c7f66b1542f84ce1d8d644970e9b935d45d21d4d143e87d94925a4bf'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return BeautifulSoup(r.text, 'lxml')

def get_temperature(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-temp')
    temperature = re.findall(r'[-]?\d{1,2}', str(buffer[0]))
    return temperature[0]

def get_weather(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-phrase')
    weather = re.findall(r'[А-Я,а-я ]', str(buffer[0]))
    return ''.join(weather)

def get_wind(html):
    buffer = html.find('div', id='hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b').find_all(class_='today_nowcard-sidecar component panel')
    wind = re.findall(r'[А-Я]{1,3} \d{1,2}', str(buffer[0]))[0]
    wind = wind.split(' ')
    return wind

def get_date(location, temp, wether, wind):
    wind_vector = wind[0]
    wind_speed = str(round(float(wind[1])/3.6, 2))
    return "Погода " + location + " сейчас:\n" + str(temp) + "°, " + str(wether) + "\nВетер " + wind_vector + " " + wind_speed + " м/с"

def moskow():
    html = get_html(url_moskow)
    return get_date('в Москве', get_temperature(html), get_weather(html), get_wind(html))

def tlt():
    html = get_html(url_tlt)
    return get_date('в Тольятти', get_temperature(html), get_weather(html), get_wind(html))

def istra():
    html = get_html(url_istra)
    return get_date('в Истре', get_temperature(html), get_weather(html), get_wind(html))

def spb():
    html = get_html(url_spb)
    return get_date('в Питере', get_temperature(html), get_weather(html), get_wind(html))