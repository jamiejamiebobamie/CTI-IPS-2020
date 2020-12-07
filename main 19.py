def find_pivot_index(input_list):
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
  min_i = 0
  for i in range(len(input_list)):
    if input_list[i] < input_list[min_i]:
      min_i = i
  return min_i
    