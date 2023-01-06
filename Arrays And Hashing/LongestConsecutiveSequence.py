class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            cur_count = 1
            temp = num+1
            while temp in nums_set:
                cur_count+=1
                temp+=1
            max_count = max(max_count, cur_count)
        return max_count