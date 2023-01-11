from collections import deque
class Solution:
    def check_all_rotten(self, grid, visited):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and visited[row][col]==0:
                    return False
        return True

    def has_zero_oranges(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]!=0:
                    return False
        return True
    

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if self.has_zero_oranges(grid):
            return 0

        visited = [[0 for col in sublist] for sublist in grid]
        queue = deque()

        #put all the starting points in a queue and run bfs
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    queue.append((row, col, 0))
                    visited[row][col] = 1

        if not queue:
            return -1
        max_level = 0
        while queue:
            row, col, level = queue[0]
            queue.popleft()
            max_level = level
            if row>0 and visited[row-1][col]==0 and grid[row-1][col]==1:
                queue.append((row-1, col, level+1))
                visited[row-1][col]=1
            if row<len(grid)-1 and visited[row+1][col]==0 and grid[row+1][col]==1:
                queue.append((row+1, col, level+1))
                visited[row+1][col]=1
            if col>0 and visited[row][col-1]==0 and grid[row][col-1]==1:
                queue.append((row, col-1, level+1))
                visited[row][col-1]=1
            if col<len(grid[0])-1 and visited[row][col+1]==0 and grid[row][col+1]==1:
                queue.append((row, col+1, level+1))
                visited[row][col+1]=1

        if not self.check_all_rotten(grid, visited):
            return -1
        return max_level