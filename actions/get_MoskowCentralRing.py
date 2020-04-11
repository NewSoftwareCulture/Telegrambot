import requests
import re
import time
from bs4 import BeautifulSoup

url_DelovoyCenter = 'https://t.rasp.yandex.ru/station/9855158/suburban/?direction=%D0%BF%D0%BE+%D1%87%D0%B0%D1%81%D0%BE%D0%B2%D0%BE%D0%B9+%D1%81%D1%82%D1%80%D0%B5%D0%BB%D0%BA%D0%B5+%28%D0%BD%D0%B0+%D0%94%D0%B5%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9+%D1%86%D0%B5%D0%BD%D1%82%D1%80%29'
url_Lushniki = 'https://t.rasp.yandex.ru/station/9855158/suburban/?direction=%D0%BF%D1%80%D0%BE%D1%82%D0%B8%D0%B2+%D1%87%D0%B0%D1%81%D0%BE%D0%B2%D0%BE%D0%B9+%D1%81%D1%82%D1%80%D0%B5%D0%BB%D0%BA%D0%B8+%28%D0%BD%D0%B0+%D0%90%D0%B2%D1%82%D0%BE%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4%D1%81%D0%BA%D1%83%D1%8E%29'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return BeautifulSoup(r.text, 'lxml')

def get_table(html):
    table = ['', '', '', '', '']
    buffer = str(html.find_all('table')[0].find_all(class_ = 'StationTable__presentThreads'))
    times = re.findall(r'\d\d:\d\d', buffer)
    date = re.findall(r'\d{1,2} [А-я]*.', buffer)[0]
    for i in range(5):
        table[i] = date + '  -  ' + times[i]
    return table

def format(location, line):
    result = location + '\n'
    for i in line:
        result += i + '\n' 
    return result[:-1]

def Lushniki():
    html = get_html(url_Lushniki)
    return format('Лужники', get_table(html))


def DelovoyCenter():
    html = get_html(url_DelovoyCenter)
    return format('Деловой центр', get_table(html))