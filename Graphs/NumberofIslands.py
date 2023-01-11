class Solution:
    def dfs(self, grid, row, col, island_number):
        if row<0 or row>=len(grid):
            return
        if col<0 or col>=len(grid[0]):
            return
        if grid[row][col]=="1":
            grid[row][col]=island_number
            self.dfs(grid, row-1, col, island_number)
            self.dfs(grid, row+1, col, island_number)
            self.dfs(grid, row, col-1, island_number)
            self.dfs(grid, row, col+1, island_number)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    self.dfs(grid, i, j, count+1)
        #print(grid)
        return count