class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left_ind, right_ind = 0, len(height)-1
        while left_ind<right_ind:
            min_height, width = min(height[left_ind], height[right_ind]), right_ind-left_ind
            cur_volume = min_height*width
            max_volume = max(max_volume, cur_volume)
            if height[left_ind]>height[right_ind]:
                right_ind-=1
            else:
                left_ind+=1
        return max_volume