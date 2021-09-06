import requests
from bs4 import BeautifulSoup

get_precio=lambda codigo: str(codigo.find('div', class_='product-info--price-new')).split("\n")[1].rsplit("<")[0].strip()[1:]
get_nombre=lambda url: " ".join(url.split(".com/")[1].split("-"))
get_producto=lambda url: get_precio(BeautifulSoup(requests.get(url).content, 'html.parser'))
get_tienda=lambda url: url.split(".com/")[0].split(".")[1]

"""url=""
print(f"El precio de {get_nombre(url)} es: {get_producto(url)} la tienda es: {get_tienda(url)}")"""

