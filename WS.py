import requests
from bs4 import BeautifulSoup

URL = 'https://www.alkosto.com/llanta-pirelli-p1-185-65r15'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
sentencias = soup.find_all('span', class_='price')
for sentencia in sentencias:
  sentencia=str(sentencia).split("span")
  for x in sentencia:
    if "itemprop=\"price\">" in x:
      precio=x.split(">")[1].rsplit("<")[0]
print("Precio del producto: "+precio)

