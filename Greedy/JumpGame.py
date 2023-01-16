class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max = nums[0]
        ind = 0
        while ind <=cur_max and cur_max<len(nums):
            print(ind, cur_max)
            if cur_max==ind and nums[ind]==0:
                break
            cur_max =  max(ind+nums[ind], cur_max)
            ind+=1
        return cur_max>=len(nums)-1