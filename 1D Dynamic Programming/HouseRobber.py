class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[-1]

        dp_arr = nums[:]
        dp_arr[1] = max(nums[:2])

        for i in range(2, len(dp_arr)):
            dp_arr[i] = max(nums[i]+dp_arr[i-2], dp_arr[i-1])
        return dp_arr[-1]