def minAddToMakeValid(S):
  stack = 0
  excess = 0
  for i in range(len(S)):
    if S[i] == "(":
      stack+=1
    else:
      if stack:
        stack-=1
      else:
        excess+=1
  return stack+excess
      
	
# sampleInput = '(())()'
# print(minAddToMakeValid(sampleInput))