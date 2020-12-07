def find_index(sorted_list, target):
  lower = 0
  upper = len(sorted_list)-1
  middle = lower + (upper - lower) // 2
  while lower < upper:
    if sorted_list[middle] == target:
      return middle
    elif target > sorted_list[middle]:
      lower = middle + 1
    else:
      upper = middle
    middle = lower + (upper - lower) // 2
  return middle if target < sorted_list[middle] else middle+1

# sorted_list = [1,3,5,6]
# target = 2
# sorted_list = [1,3,5,6]
# target = 0
# sorted_list = [1,3,5,6]
# target = 7
# sorted_list = [1,3,5,6]
# target = 4
# print(find_index(sorted_list, target))

  