def first_missing_positive_integer(integers):
  present_nums = set(integers)
  max_num = max(integers)
  for i in range(1,max_num):
    if i not in present_nums:
      return i
  return max_num+1 if max_num+1>0 else 1
  
print(first_missing_positive_integer([-8,-7,-6]))