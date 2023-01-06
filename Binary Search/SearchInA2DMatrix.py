class Solution:
    def lower_bound(self, matrix, target):
        num_rows = len(matrix)
        top, bottom = 0, num_rows-1
        while top<bottom:
            if top==bottom-1:
                if matrix[bottom][0]<=target:
                    return bottom
                else:
                    return top
            mid = (top+bottom)//2
            if target==matrix[mid][0]:
                return mid
            if target < matrix[mid][0]:
                bottom = mid-1
            else:
                top = mid
        return top
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)-1
        if matrix[-1][0]>target:
            row_num = self.lower_bound(matrix, target)
        left, right = 0, len(matrix[0])-1
        while left<=right:
            mid = (left+right)//2
            print(row_num, mid)
            if matrix[row_num][mid]==target:
                return True
            if matrix[row_num][mid]<target:
                left = mid+1
            else:
                right = mid-1
        return False