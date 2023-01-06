class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind1, ind2 = -1, -1
        num_dict = {}
        for ind, num in enumerate(nums):
            key = target-num
            if key in num_dict:
                return [num_dict[key], ind]
            else:
                num_dict[num] = ind