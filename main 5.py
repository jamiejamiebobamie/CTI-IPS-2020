def power_of_three(n):
  power = 0
  while power < n:
    test = 3**power
    if test == n:
      return True
    power+=1
  return False

# n = int(input())
print(power_of_three(45))