def backspaceCompare(String1, String2):
  i = len(String1)-1
  j = len(String2)-1
  
  i_count = 0
  j_count = 0
  
  while i >= 0 and j >= 0:
    if String1[i] != "#" or String2[j] != "#":
      if i_count or j_count:
        if i_count:
          i-=1
          i_count-=1
        else:
          j-=1
          j_count-=1
      else:
        if String1[i] == String2[j]:
          i-=1
          j-=1
        else:
          return False
    else:
      if String1[i] != "#":
        i_count+=1
        i-=1
      if String2[j] != "#":
        j_count+=1
        j-=1
    return True
    
sampleInput1A = "ab#"
sampleInput1B = "ab#"
print(backspaceCompare(sampleInput1A, sampleInput1B))
