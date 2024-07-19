class SudokuPuzzle:
    def solveSudoku(self,board):
      
        self.solve(board)
        self.print_board(board)
        
        
    def isvalid(self,board,k,row,col):
        """
        return if the number fit in the position
        param board: 2d list of strings
        param position: (row, col)
        param k: string
        rturn: boolean
        """
        for r in range(9):
           if board[r][col]==k:
              return False
        for c in range(9):
            if board[row][c]==k:
              return False
        p=row-row%3
        q=col-col%3
        # print(p,q)
        for r in range(p,p+3):
          for c in range(q,q+3):
            if board[r][c]==k:
              return False
        return True
      
    def solve(self,board):
        """
    		solve a sudoku board using backtracking
    		param board: 2d list of strings
    		return: solution
    		"""
        for i in range(9):
          for j in range(9):
              if board[i][j]=='.':
                for k in range(1,10):
                  if self.isvalid(board,str(k),i,j):
                      board[i][j]=str(k)
                      if self.solve(board):
                        return True
                      board[i][j]='.'
                return False
        return True
            
    def print_board(self,board):
        """
        prints the board
        param board: 2d List of strings
        return: None
        """
        for i in range(9):
            if i%3 == 0 and i != 0:
                print("-"*21, sep=' ', end='\n')
            for j in range(9):
                if j%3 == 0 and j != 0:
                    print('|', sep=' ', end=' ')
                print(board[i][j], sep=' ', end=' ')
            print(' ')
        
        
        
        
board=[["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]
obj=SudokuPuzzle()
obj.solveSudoku(board)

