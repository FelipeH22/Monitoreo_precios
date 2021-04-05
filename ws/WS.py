import requests
from bs4 import BeautifulSoup

get_precio=lambda codigo: str(codigo.find('span', class_='price')).split("\n")[1].rsplit("</")[0].split(">$")[1].lstrip()
get_nombre=lambda url: " ".join(url.split(".com/")[1].split("-"))
get_producto=lambda url: get_precio(BeautifulSoup(requests.get(url).content, 'html.parser'))

url='https://www.alkosto.com/ringo-croquetas-adultos-20kg'
print("El precio de "+get_nombre(url)+" es: "+get_producto(url))
