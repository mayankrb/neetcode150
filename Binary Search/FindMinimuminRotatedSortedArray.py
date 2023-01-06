class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)
        if nums[-1]>nums[0]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left<=right:
            if left>=right-1:
                return min(nums[left], nums[right])
            mid = (left+right)//2
            if nums[mid]>nums[left]:
                left = mid
            else:
                right = mid
        return nums[left]  