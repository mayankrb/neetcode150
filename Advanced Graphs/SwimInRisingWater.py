class Solution:
    def flood_fill(self, grid, visited, row, col, cur_time):
        if col<0 or row<0 or col>=len(grid[0]) or row>= len(grid):
            return
        if row>0 and grid[row-1][col]<=cur_time and visited[row-1][col]==0:
            visited[row-1][col]=1
            self.flood_fill(grid, visited, row-1, col, cur_time)
        if row<len(grid)-1 and grid[row+1][col]<=cur_time and visited[row+1][col]==0:
            visited[row+1][col]=1
            self.flood_fill(grid, visited, row+1, col, cur_time)
        if col>0 and grid[row][col-1]<=cur_time and visited[row][col-1]==0:
            visited[row][col-1]=1
            self.flood_fill(grid, visited, row, col-1, cur_time)
        if col<len(grid[0])-1 and grid[row][col+1]<=cur_time and visited[row][col+1]==0:
            visited[row][col+1]=1
            self.flood_fill(grid, visited, row, col+1, cur_time)
        return

    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid)==1:
            return 0
        min_time, max_time = grid[0][0], len(grid)**2
        while min_time<max_time:
            visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
            mid = (min_time+max_time)//2
            visited[0][0] = 0
            self.flood_fill(grid, visited, 0, 0, mid)
            if visited[-1][-1]==1:
                max_time = mid
            else:
                min_time = mid+1
        return min_time