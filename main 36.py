def simplifyPath(path):
  symbols = path.split("/")
  up_level_count = 0
  path = []
  for i in range(len(symbols)-1,0,-1):
    if symbols[i] == "..":
      up_level_count +=1
    elif symbols[i].isalnum() and not up_level_count:
      path.append(symbols[i])
    elif symbols[i].isalnum() and up_level_count:
      up_level_count -=1
  
  path = path[::-1]
  return "/"+"/".join(path)
    
testPath = "/a//b////c/d//././/.."
print(simplifyPath(testPath))