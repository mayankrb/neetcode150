class Solution:

    #uses patience sort to find lis in nlogn
    def get_lower_bound(self, arr, target):
        if arr[-1][-1]<target:
            return len(arr)

        left, right = 0, len(arr)-1
        while left<right:
            if left==right-1:
                if arr[left][-1]<target:
                    return right
                return left        
            mid = (left+right)//2
            if arr[mid][-1]<target:
                left = mid
            else:
                right = mid
        return left

    def longest_increasing_subsequence(self, checking_arr):
        temp_arr = []
        for num in checking_arr:
            if len(temp_arr)==0:
                temp_arr.append([num])
            else:
                lower_bound_ind = self.get_lower_bound(temp_arr, num)
                if lower_bound_ind==len(temp_arr):
                    temp_arr.append([])
                temp_arr[lower_bound_ind].append(num)
        print(checking_arr)
        print(temp_arr)
        return len(temp_arr)
        

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        Let the sequences be A and B.
        Define a sequence C. C[i] is the index of B[i] in A. (A[C[i]] = B[i])
        LCS of A and B is the longest increasing subsequence of C
        """
        indices_dict = {num:ind for ind, num in enumerate(target)}
        checking_arr = []
        for num in arr:
            if num in indices_dict.keys():
                checking_arr.append(indices_dict[num])
            
        return len(target)-self.longest_increasing_subsequence(checking_arr)