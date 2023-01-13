import random
import heapq
class Solution:
    def deterministic_method(self, nums, start, end, k):
        if start==end:
            return nums[start]
        start1, end1 = start, end
        pivot = random.randint(start, end)
        while start<=pivot and nums[start] <= nums[pivot]:
            start+=1
        while end >= pivot and nums[end] >= nums[pivot]:
            end-=1
        while start <= pivot:
            if nums[start] > nums[pivot]:
                nums[pivot-1], nums[pivot] = nums[pivot], nums[pivot-1]
                if pivot > start+1:
                    nums[pivot], nums[start] = nums[start], nums[pivot]
                pivot-=1
            else:
                start+=1
        while end >= pivot:
            if nums[end] < nums[pivot]:
                nums[pivot+1], nums[pivot] = nums[pivot], nums[pivot+1]
                if pivot < end-1:
                    nums[pivot], nums[end] = nums[end], nums[pivot]
                pivot+=1
            else:
                end-=1
        #print(start1, end1, pivot, k, nums[pivot])
        if pivot==k:
            return nums[pivot]
        if pivot>k:
            return self.deterministic_method(nums, start1, pivot-1, k)
        else:
            return self.deterministic_method(nums, pivot+1, end1, k)
        
    def solve_by_heap(self, nums, k):
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap, (nums[i], nums[i]))
        for i in range(k, len(nums)):
            if min_heap[0][1] < nums[i]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (nums[i], nums[i]))
        return min_heap[0][0]
            
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return self.solve_by_heap(nums, k)
        return self.deterministic_method(nums, 0, len(nums)-1, len(nums)-k)