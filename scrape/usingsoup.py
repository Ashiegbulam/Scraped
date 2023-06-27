"""Hands on some bs4 cap."""

import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.github.com/').text # access site to be scraped
soup = BeautifulSoup(site, 'lxml')


print(soup.title.string)


print(10//2)