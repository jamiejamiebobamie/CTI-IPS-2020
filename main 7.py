def last_factorial_digit(n):
  product = 1
  for i in range(1,n+1):
    product *= i
  
  return product % 10
  
print(last_factorial_digit(3))