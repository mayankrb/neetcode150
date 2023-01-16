class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps_arr = [0] + [100000 for i in range(len(nums)-1)]
        left_ptr, right_ptr = 0, 1
        while left_ptr<len(nums):
            new_right = min(len(nums), 1+left_ptr+nums[left_ptr])
            if new_right<=right_ptr:
                left_ptr+=1
                continue
            for ind in range(right_ptr, new_right):
                min_steps_arr[ind] = 1+min_steps_arr[left_ptr]
            right_ptr=new_right
            left_ptr+=1
        print(min_steps_arr)
        return min_steps_arr[-1]