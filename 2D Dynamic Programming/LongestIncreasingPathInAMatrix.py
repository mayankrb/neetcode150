class Solution:
    def dfs(self, matrix, visited, row, col, cur_depth, path_len, max_depth):
        if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]):
            return 0
        if path_len[row][col]!=-1:
            return path_len[row][col]

        visited[row][col]=1
        path_len[row][col]=1
        if row>0 and matrix[row-1][col]>matrix[row][col]:
            path_len[row][col] =  1 + self.dfs(matrix, visited, row-1, col, cur_depth+1, path_len, max_depth)
        if row<len(matrix)-1 and matrix[row+1][col]>matrix[row][col]:
            path_len[row][col] = max(path_len[row][col], 1+ self.dfs(matrix, visited, row+1, col, cur_depth+1, path_len, max_depth))
        if col>0 and matrix[row][col-1]>matrix[row][col]:
            path_len[row][col] = max(path_len[row][col], 1+ self.dfs(matrix, visited, row, col-1, cur_depth+1, path_len, max_depth))
        if col<len(matrix[0])-1 and matrix[row][col+1]>matrix[row][col]:
            path_len[row][col] = max(path_len[row][col], 1+ self.dfs(matrix, visited, row, col+1, cur_depth+1, path_len, max_depth))
        max_depth[0] = max(max_depth[0], path_len[row][col])
        return path_len[row][col]
        

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path_len = 1
        visited = [[0 for col in matrix[0]] for row in matrix]
        dp_len = [[-1 for col in matrix[0]] for row in matrix]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if visited[row][col]==1:
                    continue
                
                max_depth = [1]
                dp_len[row][col] = self.dfs(matrix, visited, row, col, 1, dp_len, max_depth)
                max_path_len = max(max_path_len, max_depth[0])
        return max_path_len