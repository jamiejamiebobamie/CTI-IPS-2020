def generate_parentheses(n):
  
  def well_formed(string):
    stack = []
    for parenthesis in string:
      if parenthesis == "(":
        stack.append(")")
      elif len(stack):
        stack.pop()
      else:
        return 0
    return 1
        
  def helper(string, open_count, close_count):
      if open_count:
        helper(string + "(", open_count-1, close_count)
      if close_count:
        helper(string+")",open_count, close_count-1)
      if not close_count and not open_count:
        if well_formed(string):
          permutations.append(string)
  
  permutations = []
  helper("", n, n)
  return permutations
  
print(generate_parentheses(3))
      