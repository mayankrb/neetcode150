class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top_left = matrix[0][0]==0
        top, left = False, False
        num_rows, num_cols = len(matrix), len(matrix[0])
        for j in range(num_cols):
            if matrix[0][j]==0:
                top=True
        for i in range(num_rows):
            if matrix[i][0]==0:
                left=True
            
        
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        print(matrix)
        for i in range(1, num_rows):
            if matrix[i][0]==0:
                for j in range(1, num_cols):
                    matrix[i][j]=0
        
        for j in range(1, num_cols):
            if matrix[0][j]==0:
                for i in range(1, num_rows):
                    matrix[i][j]=0
        
        if top_left or left:
            for i in range(num_rows):
                matrix[i][0]=0
        if top_left or top:
            for j in range(num_cols):
                matrix[0][j]=0
        

        