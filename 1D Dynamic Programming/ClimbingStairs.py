class Solution:
    def solve_dp(self, count_dict, n):
        if n<=2:
            return n
        try:
            ans = count_dict[n]
            return ans
        except:
            count_dict[n] = self.solve_dp(count_dict, n-1)+self.solve_dp(count_dict, n-2)
            return count_dict[n]

    def climbStairs(self, n: int) -> int:
        count_dict = {}
        return self.solve_dp(count_dict, n)