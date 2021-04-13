from ws import WS
import producto

def insert(url):
    try:
        producto.insert_producto(WS.get_nombre(url),WS.get_tienda(url),url)
        print("Se ingresó el producto exitosamente")
    except: print("No se pudo insertar el producto")

archivo=open("../links_pruebas.txt").read()
archivo=archivo.split("\n")
for link in archivo:
    insert(link)
