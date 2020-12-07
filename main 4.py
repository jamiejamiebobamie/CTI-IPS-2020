# Given an input, print all numbers up to and including that input,
# unless they are divisible by 3,
# then print "fizz" instead,
# or if they are divisible by 5,
# print "buzz".
# If the number is divisible by both, print "fizzbuzz".

def fizzbuzz(n):
  for i in range(1,n+1):
    if not i % 3 and not i % 5:
      print("fizzbuzz")
    elif not i % 3:
      print("fizz")
    elif not i % 5:
      print("buzz")
    else:
      print(i)


    

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)
