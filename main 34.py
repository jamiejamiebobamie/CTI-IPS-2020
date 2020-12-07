# reread problem...
def removeOuterParentheses(string):
  stack = 0
  i = 0
  units = []
  last_unit_index = 0
  included_all = False
  while i < len(string)-1:
    if string[i] == "(":
      stack+=1
    else:
      stack-=1 # assuming only valid parentheses
    if not stack:
      if i > 0:
        units.append(string[last_unit_index:i+1])
        if i == len(string)-2:
          included_all = True
        else:
          last_unit_index = i+1
    i+=1
  if not included_all:
    units.append(string[last_unit_index:])
  output_string = ""
  for unit in units:
    output_string+=unit[1:-1]
  
  return output_string
    
        
	   
	    

sampleInput = "(()())(())"
sampleInput = "(()())(())(()(()))"
print(removeOuterParentheses(sampleInput))