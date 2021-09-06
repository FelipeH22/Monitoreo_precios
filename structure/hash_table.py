import random

class hash_table:

  def __init__(self, m):
    self.p = 10000019
    self.a = random.randint(1,self.p-1)
    self.b = random.randint(0,self.p-1)
    self.m = m
    self.table = [None] * self.m

  def Hash_func(self, x):
    if (type(x) == int):
      hash = ((self.a*x+self.b)%self.p)%self.m
    else:
      hash = 0
      for i,j in enumerate(x):
        hash += (ord(j)*(self.a^i))%self.p
      hash = hash%self.m
    return hash

  def Insert(self, x):
    hash=self.Hash_func(x.key)
    if self.table[hash] == None:
      list2 = []
      list2.append(x)
      self.table[hash] = list2
    else:
      self.table[hash].append(x)

  def Search(self,x):
    hash=self.Hash_func(x)
    if (self.table[hash] != None):
      for i in self.table[hash]:
        if i.key == x:
          return i.value
    return None

  def Remove(self, x):
    hash = self.Hash_func(x)
    if (self.table[hash] != None):
      for i in self.table[hash]:
        if i.key == x:
          self.table[hash].remove(i)
          print("Elemento Eliminado Correctamente")
          return
    print("No se encontro este elemento")