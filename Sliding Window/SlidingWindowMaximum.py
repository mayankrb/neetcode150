from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums[:]
        maximum_arr = []
        dq = deque() 
        for ind, num in enumerate(nums):
            if not dq:
                dq.append([num, ind])
                continue
            while dq and dq[-1][0]<num and dq[-1][1]+k>ind:
                dq.pop()
            dq.append([num, ind])
            if ind>=k-1:
                maximum_arr.append(dq[0][0])
                if dq[0][1]<=ind-k+1:
                    dq.popleft()
        
        return maximum_arr