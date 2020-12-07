### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
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
  
  # implement this method
  def kth_from_the_end(self, k):
    # get the count of the nodes in the LL
    count = 0
    curr = self.head
    while curr:
      curr = curr.next
      count+=1
    # compute the number of nodes
      # to traverse to get to the kth node
      # from the back
    n = count - k
    # iterate to the correct node and return it
    curr = self.head
    count = 0
    while curr:
      if count == n-1:
        return curr.data
      curr = curr.next
      count+=1