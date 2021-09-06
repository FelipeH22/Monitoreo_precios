from heap import Heap
import sys
sys.path.append('../bd')
from bd import precio
from ws import ws
import time

url=input()
precios=precio.get_precios_producto(url)
heap_producto1=Heap()
for pr in precios: heap_producto1.Insert(pr)
t_0=time.time()
print(f"El precio mínimo registrado para {ws.get_nombre(url)} es: {str(heap_producto1.ExtractMin())[1:-3]}")
print('tiempo usando heap:',time.time()-t_0)
t_0_1=time.time()
menor=99999999
for pr in precios:
    if int(str(pr)[1:-3])<menor: menor=int(str(pr)[1:-3])
print(f"El precio mínimo registrado para {ws.get_nombre(url)} es: {menor}")
print('tiempo usando for:',time.time()-t_0_1)