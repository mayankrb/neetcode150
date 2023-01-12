class Solution:
    def solve(self, nums, cur_ind, dp_table, remaining_amount):
        if remaining_amount==0:
            return 1
        if cur_ind>=len(nums):
            return -1
        if dp_table[cur_ind][remaining_amount]!=0:
            return dp_table[cur_ind][remaining_amount]
        dp_table[cur_ind][remaining_amount]=-1
        dp_table[cur_ind][remaining_amount] = max(dp_table[cur_ind][remaining_amount], self.solve(nums, cur_ind+1, dp_table, remaining_amount))
        if nums[cur_ind]<=remaining_amount:
            dp_table[cur_ind][remaining_amount] = max(dp_table[cur_ind][remaining_amount], self.solve(nums, cur_ind+1, dp_table, remaining_amount-nums[cur_ind]))
        return dp_table[cur_ind][remaining_amount]
        
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2==1:
            return False
        half = total_sum//2
        dp_table = [[0 for i in range(half+1)]for j in range(len(nums))]
        ans = self.solve(nums, 0, dp_table, total_sum//2)
        return dp_table[0][half]==1