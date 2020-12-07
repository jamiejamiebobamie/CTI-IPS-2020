def wave_array(integers):
  for i in range(0,len(integers)-1,2):
    integers[i], integers[i+1] = integers[i+1], integers[i]
  return integers
    