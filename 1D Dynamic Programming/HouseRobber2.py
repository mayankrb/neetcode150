class Solution:
    def solve(self, nums, start, end):
        if end-start<3:
            return max(nums[start:end])
        dp = nums[start:end]
        dp[1] = max(dp[:2])
        #print(dp)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i]+dp[i-2], dp[i-1])
        #print(dp)
        return dp[-1] 

    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        return max(self.solve(nums, 1, len(nums)), self.solve(nums, 0, len(nums)-1))