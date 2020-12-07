def validate_sudoku_board(board):
  
  def check_row(row_i):
    filled_in = set()
    for i in range(len(board)):
      num = board[row_i][i]
      if num.isdigit():
        if num not in filled_in:
          filled_in.add(num)
        else:
          return False
    return True
    
  def check_col(col_i):
    filled_in = set()
    for i in range(len(board)):
      num = board[i][col_i]
      if num.isdigit():
        if num not in filled_in:
          filled_in.add(num)
        else:
          return False
    return True
    
  def check_square(index_i,index_j):
    filled_in = set()
    for i in range(index_i,index_i+3):
      for j in range(index_j,index_j+3):
        num = board[i][j]
        if num.isdigit():
          if num not in filled_in:
            filled_in.add(num)
          else:
            return False
    return True
  
  answer = True
  for i in range(len(board)):
    answer = check_row(i) and answer
    answer = check_col(i) and answer

  for i in range(0,len(board),3):
    for j in range(0,len(board[0]),3):
      answer = check_square(i,j) and answer

  return answer

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(validate_sudoku_board(board))

      
  