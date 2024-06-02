class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i].count(board[i][j]) != 1:
                        return False
                    
        board_ = [[0 for _ in range(9)] for _ in range(9)]            
        for i in range(9):
            for j in range(9):
                board_[i][j] = board[j][i]
                
        for i in range(9):
            for j in range(9):
                if board_[i][j] != ".":
                    if board_[i].count(board_[i][j]) != 1:
                        return False
                    
        board_3 = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                k = (i//3)*3
                k += j//3
                l = j%3 + (i%3)*3
                board_3[i][j] = board[k][l]
                
        for i in range(9):
            for j in range(9):
                if board_3[i][j] != ".":
                    if board_3[i].count(board_3[i][j]) != 1:
                        return False     
                    
        return True
            
