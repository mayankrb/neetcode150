class Solution:
    def get_tuple(self, nums):
        nums = tuple([num for num in sorted(nums)])
        return nums
    
    def get_list(self, tuples_set):
        return [list(cur_tuple) for cur_tuple in tuples_set] 
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets_set = set()
        num_max_subsets = 2**len(nums)
        for cur_num in range(num_max_subsets):
            checking_num = 1
            checking_ind = 0
            cur_subset = []
            while checking_num<=cur_num:
                if checking_num&cur_num!=0:
                    cur_subset.append(nums[checking_ind])
                checking_ind+=1
                checking_num*=2

            cur_subset = self.get_tuple(cur_subset)
            subsets_set.add(cur_subset)
        subsets_list = self.get_list(subsets_set)
        return subsets_list