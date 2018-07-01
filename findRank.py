#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Batuhan Gürses
# Search the keyword and finding out your site's keyword rank in Google Search. Command-line program.
###

from bs4 import BeautifulSoup
import requests
import time

def google(keyword,site,pageNumber):
    """ This function finds the order of the given site according to the given keyword in google search results """
    position = 0
    arr = []
    for i in range(0,pageNumber):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        url = 'https://www.google.com/search?q='+ keyword +'&start='+ str(i*10)
        req = requests.get(url,headers=headers)
        soup = BeautifulSoup(req.text,'html.parser')
        links = soup.find_all('h3', class_='r')
        for link in links:
            link = link.find('a', attrs={'class':None}) # only main links except sub menus
            if link:
                position += 1
                text = link.get('href').split('=', 1)[-1] # split '/url?q=' section of link
                head, sep, tail = text.partition('&sa') # Example --> https://www.python.org/&sa=U&ved=0ahUKEwi_pKPPtOzbAhXGZCwKHR2XDBsQFggbMAA&usg=AOvVaw2hwAasiyaZoWlA2_seq-0k
                siteLength = len(site)
                if site == head[:siteLength]: # if given site exist in search result
                    arr.append([keyword,position,head])
    return arr


check = ''
while check != 'n':
    keywords = input('-Please enter the keyword(s) you want to search. For multiple keyword please split by comma. Example --> keyword1,keyword2,keyword3\n').split(',')
    site = input('\n-Please enter the full site adress you want to search. Example --> http://www.domain.com\n')
    pageNumber = int(input('\n-Please enter the maximum page number you want to search. Example --> 6 \n'))

    for keyword in keywords:
        results = google(keyword,site,pageNumber)
        time.sleep(2)
        if not results:
            print('\nNo results for --> {}'.format(keyword))
        else:
            for i in range(0,len(results)):
                print()
                print("Keyword: {}".format(results[i][0]))
                print("Position: {}".format(results[i][1]))
                print("Link: {}".format(results[i][2]))
                print("-------------------------")
    check = input('\nAgain? Y or N\n').lower()
