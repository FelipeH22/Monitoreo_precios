class BST:

  def __init__(self):
    self.root = None

  def Find(self, k, R):
    if R.data == k:
      return R
    elif R.data > k:
      if R.left != None:
        return self.Find(k, R.left)
      return R
    else:
      if R.right != None:
        return self.Find(k, R.right)
      return R

  def Next(self, N):
    if N.right != None:
      return self.LeftDescendant(N.right)
    else:
      return self.RightAncestor(N)

  def LeftDescendant(self, N):
    if N.left == None:
      return N
    else:
      return self.LeftDescendant(N.left)

  def RightAncestor(self, N):
    if N.data < N.parent.data:
      return N.parent
    else:
      return self.RightAncestor(N.parent)

  def RangeSearch(self, x, y, R):
    L = []
    N = self.Find(x, R)
    while N.data <= y:
      if N.data >= x:
        L.append(N)
      N = self.Next(N)
    return L

  def Insert(self, k):
    if self.root == None:
      r = Node_BST(k)
      self.root = r
    else:
      P = self.Find(k, self.root)
      if (P.data != k):
        n = Node_BST(k)
        n.parent = P
        if k > P.data:
          P.right = n
        else:
          P.left = n

  def Delete(self, N):
    if N.right == None:
      if (N.left != None):
        self.Promote(N.left)
      else:
        if N.data > N.parent.data:
          N.parent.right = None
        else:
          N.parent.left = None
      N.parent = None
      N.left = None
      N.right = None
      N.data = None
    else:
      X = self.Next(N)
      N.data = X.data
      if X.right != None:
        self.Promote(X.right)
      else:
        if N.data > X.parent.data:
          X.parent.right = None
        else:
          X.parent.left = None
      X.parent = None
      X.left = None
      X.data = None
      X.right = None

  def Promote(self,N):
    P = N.parent.parent
    if N.data < P.data:
      P.left = N
    else:
      P.right = N
    N.parent = P

def InOrderTraversal(N):
  if N == None:
    return
  InOrderTraversal(N.left)
  print(N.data)
  InOrderTraversal(N.right)
