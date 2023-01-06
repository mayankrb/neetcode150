class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1]>nums[0]:
            return 0
        left, right = 0, len(nums)-1
        while left<=right:
            if left>=right-1:
                if nums[left]<nums[right]:
                    return left
                else:
                    return right
            mid = (left+right)//2
            if nums[mid]>nums[left]:
                left = mid
            else:
                right = mid
        return left
    def binary_search(self, nums, start, end, target):
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        min_ind = self.findMin(nums)
        if target<=nums[-1]:
            return self.binary_search(nums, min_ind, len(nums)-1, target)
        else:
            return self.binary_search(nums, 0, min_ind-1, target)
    