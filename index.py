import random
import sys
from urllib.parse import urlparse
from colorama import Fore, Style
import requests
import urllib3
from bs4 import BeautifulSoup
fy = Fore.YELLOW  # Yellow
fr = Style.NORMAL  # Normal style
fr = Fore.RED 

REALDISC = 'https://www.real.discount/new/page/'
DISCUD = 'https://www.discudemy.com/all/'
animation = [
    fy + fr + "[■□□□□□□□□□]",
    fy + fr + "[■■□□□□□□□□]",
    fy + fr + "[■■■□□□□□□□]",
    fy + fr + "[■■■■□□□□□□]",
    fy + fr + "[■■■■■□□□□□]",
    fy + fr + "[■■■■■■□□□□]",
    fy + fr + "[■■■■■■■□□□]",
    fy + fr + "[■■■■■■■■□□]",
    fy + fr + "[■■■■■■■■■□]",
    fy + fr + "[■■■■■■■■■□]",
    fy + fr + "[■■■■■■■■■■]",
]
def discudemy(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(DISCUD + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('section', 'card')
    for index, items in enumerate(all):
        try:
            title = items.a.text
            url2 = items.a['href']
        except:
            title = ''
            url2 = ''
        if url2 != '':
            r2 = requests.get(url2, headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            next = soup1.find('div', 'ui center aligned basic segment')
            url3 = next.a['href']
            r3 = requests.get(url3, headers=head, verify=False)
            # sys.stdout.write("\rLOADING URLS: " + animation[index % len(animation)])
            # sys.stdout.flush()
            soup3 = BeautifulSoup(r3.content, 'html.parser')
            links_ls.append(title + '||' + soup3.find('div', 'ui segment').a['href'])
    return links_ls


# def write_coupons(list_of_coupons_and_title):
#     global no
#     for indx, coupon_and_title in enumerate(list_of_coupons_and_title):
#         title, link = coupon_and_title.split('||')
#     print("title : "+ title)
#     print("url : "+link)

def wdiscudemy():
    list_of_coupons_and_title = discudemy(1)
    


wdiscudemy()

