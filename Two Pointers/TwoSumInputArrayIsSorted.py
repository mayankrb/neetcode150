#binary search solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(arr, start_ind, num):
            left_ind, right_ind = start_ind, len(arr)-1
            while left_ind<=right_ind:
                mid = (left_ind+right_ind)//2
                if arr[mid]==num:
                    return mid
                if arr[mid]>num:
                    right_ind=mid-1
                else:
                    left_ind=mid+1
            return -1

        for ind, num in enumerate(numbers):
            num_to_find = target-num
            second_ind = binary_search(numbers, ind+1, num_to_find)
            if second_ind!=-1:
                return [ind+1, second_ind+1]
            
#two pointers solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ind, right_ind = 0, len(numbers)-1
        while left_ind<right_ind:
            if numbers[left_ind]+numbers[right_ind]==target:
                break
            if numbers[left_ind]+numbers[right_ind]<target:
               left_ind+=1
            else:
                right_ind-=1
        return [left_ind+1, right_ind+1]