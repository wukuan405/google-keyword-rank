#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author: Batuhan Gürses
"""
    Search the keyword and finding out
    your site's keyword rank in Google Search. Command-line program.
"""
from bs4 import BeautifulSoup
import requests
import time


def google(keyword, site, page_number):
    """
        This function finds the order of the given site
        according to the given keyword in google search results.
    """
    position = 0
    arr = []
    site_length = len(site)
    for i in range(0, page_number):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
             }
        url = 'https://www.google.com/search?q=' + keyword.replace(' ','+') + '&oq=' + keyword.replace(' ','+') + '&start=' + str(i*10)
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        links = soup.find_all('div', class_='r')
        for link in links:
            link = link.find('a', attrs={'class': None}).get('href')  # only main links except sub menus
            if link:
                position += 1
                if site == link[:site_length]:  # if given site exist in search result
                    arr.append([keyword, position, link])
    return arr

check = ''
while check != 'n':
    keywords = input('-Please enter the keyword(s) you want to search. For multiple keyword please split by comma. Example --> keyword1,keyword2,keyword3\n').split(',')
    site = input('\n-Please enter the full site adress you want to search. Example --> http://www.domain.com\n')
    page_number = int(input('\n-Please enter the maximum page number you want to search. Example --> 6 \n'))

    for keyword in keywords:
        results = google(keyword, site, page_number)
        time.sleep(2)
        if not results:
            print('\nNo results for --> {}'.format(keyword))
        else:
            for i in range(0, len(results)):
                print()
                print("Keyword: {}".format(results[i][0]))
                print("Position: {}".format(results[i][1]))
                print("Link: {}".format(results[i][2]))
                print("-------------------------")
    check = input('\nAgain? Y or N\n').lower()
