def pascal_triangle(numRows):
  result = []
  for r in range(numRows):
    row = []
    i = 0
    new_term = 1
    while len(row) < r+1:
      term1 = 0
      if r > 0:
        if i > 0:
          if i < len(result[r-1]):
            term1 = result[r-1][i]
          new_term = term1+result[r-1][i-1]
        i+=1
      row.append(new_term)
    result.append(row)
  
  return result

# print(pascal_triangle(5))