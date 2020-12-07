# find the pallindrome within the string
# all letters to the right of the pallindrome are considered part of the
  # pallindrome
# determine how many characters on the right do not match on the left.

def pseudo_ceildiv(a,b):
  return a//b+1

def minimumCharacters(s):
  index = -1
  i = 0
  j = len(s)-1
  while (i < j):
    print(s[i:j])
    if s[i] == s[j]:
      if index == -1:
        index = j
      i+=1
    else:
      index = -1
      j += i
      i = 0
    j-=1
  return len(s) - 1 - index if index != -1 else pseudo_ceildiv(len(s),2)
      
print(minimumCharacters("AACECAAAA"))