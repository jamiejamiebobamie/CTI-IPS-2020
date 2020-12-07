def dailyTemperatures(dailyTemps):
  arr = [None]*len(dailyTemps)
  for i, curr_temp in enumerate(dailyTemps):
    j = i
    while j < len(dailyTemps):
      if curr_temp < dailyTemps[j]:
        arr[i] = j-i
        break
      j+=1
    if not arr[i]:
      arr[i] = 0
  return arr
	  

sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))