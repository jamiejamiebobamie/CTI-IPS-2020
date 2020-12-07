class MinStack(object):

    def __init__(self):
      self.stack = []
      self.length = 0
      self.min_value = float("inf")

    def push(self, x):
      self.length += 1
      self.stack.append(x)
      if x<self.min_value:
        self.min_value = x
        
    def pop(self):
      self.length -= 1
      return self.stack.pop()

    def top(self):
      return self.stack[self.length-1]
      
    def getMin(self):
      return self.min_value

        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()