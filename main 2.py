# Determine if the input number is prime 
def isPrime(n):
  for current_number in range(2,n):
    if not n % current_number:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
  count = 0
  for i in range(2,n):
    if isPrime(i):
      count+=1
  return count
  
print(countPrimes(10))