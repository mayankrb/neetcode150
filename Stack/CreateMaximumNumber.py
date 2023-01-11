from collections import deque
class Solution:
    def get_max_stack(self, nums, k):
        min_stack = []
        if len(nums)==k:
            return nums[:]
        for i in range(len(nums)):
            if not min_stack:
                min_stack.append(nums[i])
                continue
            if k==len(min_stack) + len(nums)-i:
                    ans = list(min_stack)
                    ans.extend(nums[i:])
                    return ans
            while min_stack and min_stack[-1]<nums[i]:
                if k==len(min_stack) + len(nums)-i:
                    ans = list(min_stack)
                    ans.extend(nums[i:])
                    return ans
                min_stack.pop()
            min_stack.append(nums[i])
            #print("Here is the min stack for this size", i, min_stack)
        ans = list(min_stack)
        return ans[:k]

    def is_new_ans_larger(self, nums1, nums2):
        for ind, num in enumerate(nums1):
            if nums1[ind]==nums2[ind]:
                continue
            if nums1[ind] > nums2[ind]:
                return False
            else:
                return True
        return False

    def get_preference(self, nums1, nums2, ind1, ind2):
        while ind1<len(nums1) and ind2<len(nums2):
            if nums1[ind1]==nums2[ind2]:
                ind1+=1
                ind2+=1
                continue
            if nums1[ind1]>nums2[ind2]:
                return 1
            else:
                return 2
        if ind1==len(nums1):
            return 2
        return 1

    def get_possible_new_ans(self, stack1, stack2, k, arr):
        stack1 = list(stack1)
        stack2 = list(stack2)
        ans = []
        ind1, ind2 = 0, 0
        while k>0 and ind1<len(stack1) and ind2<len(stack2):
            print(ind1, ind2, stack1[ind1], stack2[ind2])
            if stack1[ind1]>stack2[ind2]:
                arr.append(stack1[ind1])
                ind1+=1
            elif stack1[ind1]<stack2[ind2]:
                arr.append(stack2[ind2])
                ind2+=1
            else:
                preference = self.get_preference(stack1, stack2, ind1, ind2)
                if preference==1:
                    arr.append(stack1[ind1])
                    ind1+=1
                else:
                    arr.append(stack2[ind2])
                    ind2+=1
            k-=1

        while k>0 and ind1<len(stack1):
            arr.append(stack1[ind1])
            ind1+=1
            k-=1
        while k>0 and ind2<len(stack2):
            arr.append(stack2[ind2])
            ind2+=1
            k-=1
        return
        

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if k==len(nums1)+len(nums2):
            ans = [] 
            self.get_possible_new_ans(nums1, nums2, k, ans)
            return ans
        start, end = 0, len(nums1)
        max_array = [-1 for i in range(k)]
        for possible_size in range(start, end):
            stack1 = self.get_max_stack(nums1, possible_size)
            if k-possible_size>len(nums2):
                continue
            stack2 = self.get_max_stack(nums2, k-possible_size)
            #print(possible_size, stack1, stack2)
            possible_new_ans_arr = []
            self.get_possible_new_ans(stack1, stack2, k, possible_new_ans_arr)
            if self.is_new_ans_larger(max_array, possible_new_ans_arr):
                max_array[:] = possible_new_ans_arr[:]

        nums2, nums1 = nums1, nums2
        start, end = 0, len(nums1)
        for possible_size in range(start, end):
            stack1 = self.get_max_stack(nums1, possible_size)
            if k-possible_size>len(nums2):
                continue
            stack2 = self.get_max_stack(nums2, k-possible_size)
            #print(possible_size, stack1, stack2)
            possible_new_ans_arr = []
            self.get_possible_new_ans(stack1, stack2, k, possible_new_ans_arr)
            if self.is_new_ans_larger(max_array, possible_new_ans_arr):
                max_array[:] = possible_new_ans_arr[:]
        
        return max_array