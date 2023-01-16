class Solution:
    def solve_dp(self, m, n, dp_table):
        if m<0 or n<0:
            return 0
        if m==0 or n==0:
            return 1
        if dp_table[m][n]!=-1:
            return dp_table[m][n]
        
        dp_table[m][n] = self.solve_dp(m-1, n, dp_table) + self.solve_dp(m, n-1, dp_table)
        return dp_table[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        dp_table = [[-1 for j in range(n)] for i in range(m)]
        dp_table[m-1][n-1] = self.solve_dp(m-1, n-1, dp_table)
        print(dp_table)
        return dp_table[-1][-1]