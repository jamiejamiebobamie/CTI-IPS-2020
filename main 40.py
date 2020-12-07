### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  def insert(self, data, index):
    node = LinkedNode(data)
    if index == 0:
      temp = self.head
      self.head = node
      node.next = temp
    else:
      count = 0
      curr = self.head
      prev = None
      inserted = False
      while curr:
        if count == index:
          prev.next = node
          node.next = curr
          inserted = True
        count+=1
        prev = curr
        curr = curr.next
      if not inserted:
        self.tail.next = node
        self.tail = node
        
      

    