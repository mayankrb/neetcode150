class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3:
            return min(cost)
        dp_arr = cost[:] + [0]
        for i in range(2, len(dp_arr)):
            dp_arr[i]+=min(dp_arr[i-1], dp_arr[i-2])
        return dp_arr[-1]
        