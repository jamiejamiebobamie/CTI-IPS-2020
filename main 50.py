def min_xor_value(nums):
  min_xor = float("inf")
  for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
      print(num1, num2, num1 ^ num2)
      if i != j:
        min_xor = min(min_xor, num1 ^ num2)
  return min_xor
  
nums = [0,2,5,7]
print(min_xor_value(nums))
