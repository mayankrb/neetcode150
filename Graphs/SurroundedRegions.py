class Solution:
    def flood_fill(self, board, visited, row, col):
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
            return 
        visited[row][col] = 1
        if row>0 and board[row-1][col]==0 and visited[row-1][col]==0:
            self.flood_fill(board, visited, row-1, col)
        if row<len(board)-1 and board[row+1][col]==0 and visited[row+1][col]==0:
            self.flood_fill(board, visited, row+1, col)
        if col>0 and board[row][col-1]==0 and visited[row][col-1]==0:
            self.flood_fill(board, visited, row, col-1)
        if col<len(board[0])-1 and board[row][col+1]==0 and visited[row][col+1]==0:
            self.flood_fill(board, visited, row, col+1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = [[0 for col in cur_row] for cur_row in board]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=="X":
                    board[row][col]=1
                else:
                    board[row][col]=0

        
        for row in range(len(visited)):
            if visited[row][0]==0 and board[row][0]==0:
                self.flood_fill(board, visited, row, 0)
            if visited[row][-1]==0 and board[row][-1]==0:
                self.flood_fill(board, visited, row, len(board[0])-1)
        for col in range(len(visited[0])):
            if visited[0][col]==0 and board[0][col]==0:
                self.flood_fill(board, visited, 0, col)
            if visited[-1][col]==0 and board[-1][col]==0:
                self.flood_fill(board, visited, len(board)-1, col)

        for row in range(len(visited)):
            for col in range(len(visited[0])):
                if visited[row][col]==1:
                    board[row][col]="O"
                else:
                    board[row][col]="X"
        