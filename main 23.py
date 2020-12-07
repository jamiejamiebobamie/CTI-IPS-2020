def matrix_search(matrix, target):
  lower_row = 0
  upper_row = len(matrix)
  middle_row = lower_row + (upper_row-lower_row)//2
  while lower_row < upper_row:
    lower_col = 0
    upper_col = len(matrix[0])# assuming all rows in the matrix have the same number of elements
    middle_col = lower_col + (upper_col-lower_col)//2
    while lower_col < upper_col:
      if target == matrix[middle_row][middle_col]:
        return 1
      elif target > matrix[middle_row][middle_col]:
        lower_col = middle_col+1
      else:
        upper_col = middle_col
      middle_col = lower_col + (upper_col-lower_col)//2
    if target == matrix[middle_row][0]:
      return 1
    elif target < matrix[middle_row][0]:
      upper_row = middle_row
    else:
      lower_row = middle_row+1
    middle_row = lower_row + (upper_row-lower_row)//2
  return 0
    

# matrix = [
#           [1,3,5,7],
#           [10,11,16,20],
#           [23,30,34,50],
#             ]
# print(matrix_search(matrix, 4))
