class Solution:
    
    def dfs(self, grid, row, col, cur_area):
        if row<0 or row>=len(grid):
            return
        if col<0 or col>=len(grid[0]):
            return
        if grid[row][col]==1:
            grid[row][col]=0
            cur_area[0]+=1
            self.dfs(grid, row-1, col, cur_area)
            self.dfs(grid, row+1, col, cur_area)
            self.dfs(grid, row, col-1, cur_area)
            self.dfs(grid, row, col+1, cur_area)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                cur_area = [0]
                self.dfs(grid, i, j, cur_area)
                max_area = max(max_area, cur_area[0])
        return max_area