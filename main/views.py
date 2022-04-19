from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import random



def index(request):
    page = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(page.text)
    i = int(random.uniform(8, 228))
    h = soup.find_all('tr')

    t1 = h[i].find_all('td')[1].text
    t2 = h[i].find_all('td')[2].text
    t3 = h[i].find_all('td')[3].text
    t4 = h[i].find_all('td')[4].text
    t5 = h[i].find_all('td')[5].text
    t6 = h[i].find_all('td')[6].text
    t7 = h[i].find_all('td')[7].text
    t8 = h[i].find_all('td')[8].text
    t9 = h[i].find_all('td')[9].text
    t10 = h[i].find_all('td')[10].text
    t11 = h[i].find_all('td')[11].text
    t12 = h[i].find_all('td')[12].text
    t13 = h[i].find_all('td')[13].text
    t14 = h[i].find_all('td')[14].text

    w1 = h[8].find_all('td')[1].text
    w2 = h[8].find_all('td')[2].text
    w3 = h[8].find_all('td')[3].text
    w4 = h[8].find_all('td')[4].text
    w5 = h[8].find_all('td')[5].text
    w6 = h[8].find_all('td')[6].text
    w7 = h[8].find_all('td')[7].text
    w8 = h[8].find_all('td')[8].text
    w9 = h[8].find_all('td')[9].text
    w10 = h[8].find_all('td')[10].text
    w11 = h[8].find_all('td')[11].text
    w12 = h[8].find_all('td')[12].text
    w13 = h[8].find_all('td')[13].text
    w14 = h[8].find_all('td')[14].text

    data = {
        't1': t1,
        't2': t2,
        't3': t3,
        't4': t4,
        't5': t5,
        't6': t6,
        't7': t7,
        't8': t8,
        't9': t9,
        't10': t10,
        't11': t11,
        't12': t12,
        't13': t13,
        't14': t14,
        'w1': w1,
        'w2': w2,
        'w3': w3,
        'w4': w4,
        'w5': w5,
        'w6': w6,
        'w7': w7,
        'w8': w8,
        'w9': w9,
        'w10': w10,
        'w11': w11,
        'w12': w12,
        'w13': w13,
        'w14': w14
    }

    return render(request, 'main/index.html', data)
