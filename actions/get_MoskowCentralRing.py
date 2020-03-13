import requests
import re
from bs4 import BeautifulSoup

url_DelovoyCenter = 'https://t.rasp.yandex.ru/station/9855158/suburban/?direction=%D0%BF%D0%BE+%D1%87%D0%B0%D1%81%D0%BE%D0%B2%D0%BE%D0%B9+%D1%81%D1%82%D1%80%D0%B5%D0%BB%D0%BA%D0%B5+%28%D0%BD%D0%B0+%D0%94%D0%B5%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9+%D1%86%D0%B5%D0%BD%D1%82%D1%80%29'
url_Lushniki = 'https://t.rasp.yandex.ru/station/9855158/'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return BeautifulSoup(r.text, 'lxml')

def get_header(html):
    header = ['' , '', '', '', '']
    i = 0
    while i < 5:
        time = str(html.find_all(class_ = 'b-routers__time b-routers__time_type_before-departure-left')[i])
        time = re.findall(r'\d{1,2}', time)
        if len(time) == 2:
            header[i] = 'через ' + time[0] + ' ч. ' + time[1] + ' мин.'
        else:
            header[i] = 'через ' + time[1] + ' минут'
        i += 1
    return header

def get_table(html):
    table = ['', '', '', '', '']
    number = 0
    month = ''
    i = 0
    while i < 5:
        buffer = str(html.find_all(class_ = 'b-routers__time b-routers__time_type_departure')[i])
        if i == 0: 
            number = str(re.findall(r'\d{1,2}', buffer)[0])
            month = ''.join(re.findall(r'[а-я]', buffer))
        time = str(re.findall(r'\d\d:\d\d', buffer)[0])
        table[i] = number + ' ' + month + '  -  ' + time
        i += 1
    return table

def format(location, header, table):
    i = 0
    result = location + '\n'
    while i < 5:
        result += table[i] + ' (' + header[i] + ')'
        if i < 4: result += '\n'
        i += 1
    return result


def Lushniki():
    html = get_html(url_Lushniki)
    return format('Лужники', get_header(html), get_table(html))


def DelovoyCenter():
    html = get_html(url_DelovoyCenter)
    return format('Деловой центр', get_header(html), get_table(html))