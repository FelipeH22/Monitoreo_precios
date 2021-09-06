from node_hash import node_hash
from hash_table import hash_table
import sys
sys.path.append('../bd')
from bd import persona
import time

usr='MarleneThomasIsaacsWare4017846@monitoreo_precios.co'
#Hash Table
hash_personas=hash_table(50)
personas=persona.get_personas()
for per in personas:
    node=node_hash(per[0],per[1])
    hash_personas.Insert(node)

t_hash=time.time()
clave=hash_personas.Search(usr)
print(f"clave {clave[0:5]+'***'+clave[-5:]} de {usr[0:6]+'***'+usr[-17:]} econtrada en: {time.time()-t_hash} segundos entre {len(personas)} usuarios usando HashTable")

#Array
t_arr=time.time()
for per in personas:
    if per[0]==usr: clave_arr=per[1]
    else: clave_arr=None
t_finala=time.time()
print(f"clave {clave[0:5]+'***'+clave[-5:]} de {usr[0:6]+'***'+usr[-17:]} econtrada en: {t_finala-t_arr} segundos entre {len(personas)} usuarios usando Array")