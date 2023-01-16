class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num_subsets = 2**(len(nums))
        subsets = []
        for cur_num in range(num_subsets):
            checking_num = 1
            cur_subset = []
            cur_ind = 0
            while checking_num<=cur_num:
                if cur_num & checking_num!=0:
                    cur_subset.append(nums[cur_ind])
                checking_num = checking_num*2
                cur_ind += 1
            subsets.append(cur_subset)
        return subsets