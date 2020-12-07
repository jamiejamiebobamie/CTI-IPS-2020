def longest_palindrome(input_string):
  my_palls = set()
  for i in range(len(input_string)):
    # "double letter" starters
    j=i
    k=i+1
    test = ""
    while j >= 0 and k < len(input_string):
      if input_string[j] == input_string[k]:
        if input_string[j] == " ":
          pass
        else:
          test = input_string[j]+test+input_string[k]
          my_palls.add(test)
        j-=1
        k+=1
      else:
        break
    # "single letter" starters
    j=i 
    k=i
    test = ""
    while j >= 0 and k < len(input_string):
      if input_string[j] == input_string[k]:
        if j == k:
          test+=input_string[j]
        elif input_string[j] == " ":
          pass
        else:
          test = input_string[j]+test+input_string[k]
          my_palls.add(test)
        j-=1
        k+=1
      else:
        break

  max_length_pall = ""
  for pall in my_palls:
    if len(pall) >= len(max_length_pall):
      max_length_pall = pall
  return max_length_pall

input_string = "abba is babaabab"
print(longest_palindrome(input_string))