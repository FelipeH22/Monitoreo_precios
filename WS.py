import requests
from bs4 import BeautifulSoup

URL = 'https://www.alkosto.com/llanta-pirelli-p1-185-65r15'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
job_elems = soup.find_all('span', class_='price')
for job_elem in job_elems:
  job_elem=str(job_elem).split("span")
  for x in job_elem:
    if "itemprop=\"price\">" in x:
      precio=x.split(">")[1].rsplit("<")[0]
print("Precio del producto: "+precio)

