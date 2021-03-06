class Stack:
  def __init__(self):
    self.top = None

  def push(self, item):
    node = Node(item)
    node.next = self.top
    self.top = node

  
  def pop():
    if self.empty():
      print("The stack has no element to pop")
      node = Node(None)
      return node
    else:
      node = self.top
      self.top = self.top.next
      return node
  
  def top():
    if self.empty():
      print("The stack has no element")
    else:
      return self.top
  
  def empty(self):
    if self.top is None:
      return True
    else:
      return False    
