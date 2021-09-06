class Heap:
  def __init__(self):
    self.H = []
  def Parent(self, i):
    return (i-1)//2
  def LeftChild(self, i):
    return 2*i+1
  def RightChild(self, i):
    return 2*i+2
  def SiftUp(self, i):
    while (i>0 and self.H[self.Parent(i)] > self.H[i]):
      self.H[self.Parent(i)], self.H[i] = self.H[i], self.H[self.Parent(i)]
      i = self.Parent(i)
  def SiftDown(self, i):
    min = i
    l = self.LeftChild(i)
    if (l < len(self.H) and self.H[l] < self.H[min]):
      min = l
    r = self.RightChild(i)
    if (r < len(self.H) and self.H[r] < self.H[min]):
      min = r
    if i != min:
      self.H[i], self.H[min] = self.H[min], self.H[i]
      return self.SiftDown(min)
  def Insert(self, p):
    self.H.append(p)
    self.SiftUp(len(self.H)-1)
  def ExtractMin(self):
    r = self.H[0]
    self.H[0] = self.H[len(self.H)-1]
    self.H.pop()
    self.SiftDown(0)
    return r
  def Remove(self, i):
    self.H[i] = -99999999999999999
    self.SiftUp(i)
    self.ExtractMin()
  def ChangePriority(self, i, p):
    oldP = self.H[i]
    self.H[i] = p
    if p > oldP:
      self.SiftDown(i)
    else:
      self.SiftUp(i)