class Solution:
    def permute_helper(self, nums, ans_arr, cur_ind):
        if cur_ind==len(nums):
            ans_arr.append(nums[:])
            return
        for ind in range(cur_ind, len(nums)):
            nums[cur_ind], nums[ind] = nums[ind], nums[cur_ind]
            self.permute_helper(nums, ans_arr, cur_ind+1)
            nums[cur_ind], nums[ind] = nums[ind], nums[cur_ind]
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permute_helper(nums, permutations, 0)
        return permutations