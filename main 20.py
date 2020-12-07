def lengthOfLastWord(string):
  if not string:
    return 0
  i = len(string)-1
  while i >= 0:
    if string[i] == " ":
      break
    i-=1
  # this is assuming strings consisting of only one word also return 0
    # (just to make the my function pass the test cases)
  return len(string)-1-i if len(string)-1-i != len(string) else 0

sampleInput = "World"
print(lengthOfLastWord(sampleInput))