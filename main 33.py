def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a//b

def evaluate_expression(expression):
  operation_lookup = {"+":add,"-":subtract,"*":multiply,"/":divide}
  answer = None
  stack = []
  for e in expression:
    if e.isdigit():
      stack.append(e)
    else:
      operation = operation_lookup[e]
      a = answer
      if stack:
        b = int(stack.pop())
      if stack:
        a = int(stack.pop())
      answer = operation(a,b)
    
  return answer
      
      

expression = ["88", "2", "/", "2","*"]
print(evaluate_expression(expression))