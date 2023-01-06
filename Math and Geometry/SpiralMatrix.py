class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order_list = []
        start_row, end_row = 0, len(matrix)-1
        start_col, end_col = 0, len(matrix[0])-1
        while start_row<=end_row and start_col<=end_col:
            i =  start_row
            j = start_col

            if start_row==end_row:
                while j<=end_col:
                    spiral_order_list.append(matrix[i][j])
                    j+=1
                break
            if start_col==end_col:
                while i<=end_row:
                    spiral_order_list.append(matrix[i][j])
                    i+=1
                break

            while j<=end_col:
                spiral_order_list.append(matrix[i][j])
                j+=1
            i+=1
            j-=1
            while i<=end_row:
                print(i, j)
                spiral_order_list.append(matrix[i][j])
                i+=1
            j-=1
            i-=1
            while j>=start_col and i>start_row:
                spiral_order_list.append(matrix[i][j])
                j-=1
            j+=1
            i-=1
            while i>start_row and j>=start_col:
                spiral_order_list.append(matrix[i][j])
                i-=1
            start_row+=1
            start_col+=1
            end_row-=1
            end_col-=1
            #print(spiral_order_list)
        return spiral_order_list
            