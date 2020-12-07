def search_for_range(array, target):
  lower = 0
  upper = len(array)-1
  middle = lower+ (upper-lower)//2
  while lower < upper:
    if target == array[middle]:
      go_low = middle
      go_high = middle
      while go_low >= 0:
        if array[go_low - 1] == target:
          go_low-=1
        else:
          break
      while go_high < len(array):
        if array[go_high + 1] == target:
          go_high+=1
        else:
          break
      return [go_low,go_high]
    elif target > array[middle]:
      lower = middle+1
    else:
      upper = middle-1
    middle = lower + (upper-lower)//2
  return [-1,-1]
      
arr = [5,7,7,8,8,10]
print(search_for_range(arr, 8))
          


  