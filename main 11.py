def rotate_array(input_array, k):
  k = k % len(input_array)
  
  for i in range(k):
    input_array.insert(0,input_array[-1])
    input_array.pop()
  return input_array[k:]

