class Solution:
    def check_rows(self, board):
        valid_rows_flag = True
        for row_num in range(9):
            cur_visited = [0 for i in range(10)]
            for col_num in range(9):
                if board[row_num][col_num]==".":
                    continue
                if cur_visited[int(board[row_num][col_num])]==1:
                    valid_rows_flag=False
                    break
                else:
                    cur_visited[int(board[row_num][col_num])]=1
            if not valid_rows_flag:
                break
        return valid_rows_flag 

    def check_columns(self, board):
        valid_cols_flag = True
        for col_num in range(9):
            cur_visited = [0 for i in range(10)]
            for row_num in range(9):
                if board[row_num][col_num]==".":
                    continue
                if cur_visited[int(board[row_num][col_num])]==1:
                    valid_cols_flag=False
                    break
                else:
                    cur_visited[int(board[row_num][col_num])]=1

            if not valid_cols_flag:
                break
        return valid_cols_flag 
        
    def check_mini_squares(self, board):
        valid_mini_squares_flag = True
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                cur_visited = [0 for i in range(10)]
                for row_offset in range(3):
                    for col_offset in range(3):
                        if board[start_row+row_offset][start_col+col_offset]==".":
                            continue
                        digit = int(board[start_row+row_offset][start_col+col_offset])
                        #print(digit)
                        if cur_visited[digit]==1:
                            valid_mini_squares_flag=False
                            break
                        else:
                            cur_visited[digit]=1
                    if valid_mini_squares_flag==False:
                        break
                if valid_mini_squares_flag==False:
                        break
            if valid_mini_squares_flag==False:
                        break
        return valid_mini_squares_flag
                

                        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_sudoku_flag = True
        valid_sudoku_flag = self.check_mini_squares(board) and self.check_rows(board) and self.check_columns(board)
        return valid_sudoku_flag
