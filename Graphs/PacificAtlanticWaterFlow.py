class Solution:
    def flood_fill(self, heights, is_possible_grid, visited, row, col):
        if row<0 or row>=len(heights) or col<0 or col>=len(heights[0]):
            return 
        is_possible_grid[row][col]=1
        visited[row][col] = 0
        if row>0 and heights[row-1][col]>=heights[row][col] and is_possible_grid[row-1][col]==0:
            self.flood_fill(heights, is_possible_grid, visited, row-1, col)
        if row<len(heights)-1 and heights[row+1][col]>=heights[row][col] and is_possible_grid[row+1][col]==0:
            self.flood_fill(heights, is_possible_grid, visited, row+1, col)
        if col>0 and heights[row][col-1]>=heights[row][col] and is_possible_grid[row][col-1]==0:
            self.flood_fill(heights, is_possible_grid, visited, row, col-1)
        if col<len(heights[0])-1 and heights[row][col+1]>=heights[row][col] and is_possible_grid[row][col+1]==0:
            self.flood_fill(heights, is_possible_grid, visited, row, col+1)
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_atlantic = [[0 for num in sublist] for sublist in heights]
        can_reach_pacific = [[0 for num in sublist] for sublist in heights]
        visited_pacific = [[0 for num in sublist] for sublist in heights]
        visited_atlantic = [[0 for num in sublist] for sublist in heights]
        ans = []

        for row in range(len(heights)):
            can_reach_atlantic[row][-1]=1
            can_reach_pacific[row][0] = 1
        for col in range(len(heights[0])):
            can_reach_atlantic[-1][col]=1
            can_reach_pacific[0][col] = 1

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if can_reach_atlantic[row][col]==1 and visited_atlantic[row][col]==0:
                    self.flood_fill(heights, can_reach_atlantic, visited_atlantic, row, col)
                if can_reach_pacific[row][col]==1 and visited_pacific[row][col]==0:
                    self.flood_fill(heights, can_reach_pacific, visited_pacific, row, col)
        
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if can_reach_atlantic[row][col]==1 and can_reach_pacific[row][col]==1:
                    ans.append([row, col])
        return ans