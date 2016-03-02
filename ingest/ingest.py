
"""
A module to download restaurants information
"""

from lxml import html
import requests
import json
from bs4 import BeautifulSoup
import urllib.request

def html_to_soup(self, rest_url='http://www.allmenus.com/dc/washington/-/?sort=popular'):
    html = urllib.request.urlopen(rest_url).read()
    soup = BeautifulSoup(html, "lxml")
    for h2 in soup.findAll("a", href=True):
    if (h2['href'])[:3] == '/dc':
        url_list.append(h2['href'])

def soup_to_urllist(self, soup):
    url_list = []
    for u in soup.findAll("a", href=True):
    if (u['href'])[:3] == '/dc':
        url_list.append(u['href'])
    return url_list

#html = urllib.request.urlopen('http://www.allmenus.com'+url_list[0]).read()
#soup = BeautifulSoup(html, "lxml")
#items = [h2.string for h2 in soup.findAll("span", "name")]
#prices = [h2.string for h2 in soup.findAll("span", "price")]
#descriptions = [h2.string for h2 in soup.findAll("p", "description")]
#print(descriptions)
