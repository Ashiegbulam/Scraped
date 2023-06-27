"""Script to get a list of houses in the jersey city of Nj with their prices 
and address from the zillow real estate website."""

import requests
from bs4 import BeautifulSoup

zillow = requests.get('https://www.zillow.com/')
print(zillow)
# sieve price from provided dropdown
# collect required data
# get link and loop through to collect multi pagenated data
print(10//2)