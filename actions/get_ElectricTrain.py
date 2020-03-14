import requests
import re
from bs4 import BeautifulSoup
import time

url_Streshnevo_Istra = 'https://www.tutu.ru/rasp.php?st1=36105&st2=37705'
url_Tushino_Istra = 'https://www.tutu.ru/rasp.php?st1=36305&st2=37705'
url_Dmitrovskaya_Istra = 'https://www.tutu.ru/rasp.php?st1=35805&st2=37705'
url_Istra_Streshnevo = 'https://www.tutu.ru/rasp.php?st1=37705&st2=36105'
url_Istra_Tushino = 'https://www.tutu.ru/rasp.php?st1=37705&st2=36305'
url_Istra_Dmitrovskaya = 'https://www.tutu.ru/rasp.php?st1=37705&st2=35805'

def get_html(url):
    r = requests.get(url)    
    r.encoding = 'utf8'
    return BeautifulSoup(r.text, 'lxml')

def get_table(html):
    buffer = html.find_all(class_ = 'desktop__card__yoy03')
    size = 10
    array = ['', '', '', '', '', '', '', '', '', '']
    i = 0
    for it in buffer:
        time_now = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min)
        time_table = re.findall(r'\d\d:\d\d', str(it))
        if len(time_table) != 0 and time_table[0] > time_now and i < size:
            type_train = re.findall(r'\b(Стандарт|Скорый)\b', str(it))
            station = re.findall(r'[А-я]{4,}[ (А-я.]*[ А-я)]*', str(it))
            array[i] = time_table[0] + " -> " + time_table[1] + ' (' +  type_train[0] + ') \t' + station[2] + ' -> ' + station[3]
            i += 1

    return array

def format(point_A, point_B, array):
    result = point_A + ' -> '+ point_B + '\n'
    for it in array:
        result += it + '\n'
    result = result[0:-2]
    return result


def Streshnevo_Istra():
    html = get_html(url_Streshnevo_Istra)
    return format('Стрешнево', 'Истра', get_table(html))

def Tushino_Istra():
    html = get_html(url_Tushino_Istra)
    return format('Тушино', 'Истра', get_table(html))

def Dmitrovskaya_Istra():
    html = get_html(url_Dmitrovskaya_Istra)
    return format('Дмитровская', 'Истра', get_table(html))

def Istra_Streshnevo():
    html = get_html(url_Istra_Streshnevo)
    return format('Истра', 'Стрешнево', get_table(html))

def Istra_Tushino():
    html = get_html(url_Istra_Tushino)
    return format('Истра', 'Тушино', get_table(html))

def Istra_Dmitrovskaya():
    html = get_html(url_Istra_Dmitrovskaya)
    return format('Истра', 'Дмитровская', get_table(html))