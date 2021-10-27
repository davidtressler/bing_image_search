import requests
from bs4 import BeautifulSoup
import random


query = "huskies"

url= f"http://www.bing.com/images/search?q={query}" #+ "&FORM=HDRSC2"

print(url)
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
filter_result = soup.find_all(class_='iusc')
s = str(filter_result[random.randint(0,len(filter_result))])
x = s.split()


for i in x:
    if "murl" in i:
        bar = i.split('murl')

        final_result = bar[1][3:].split('"')
        print(final_result[0])
