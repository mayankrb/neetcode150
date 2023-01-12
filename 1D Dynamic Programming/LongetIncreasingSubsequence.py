class Solution:
    def get_ind(self, num, patience_sort_list):
        if len(patience_sort_list)>0 and patience_sort_list[-1][-1] < num:
            return len(patience_sort_list)
        
        left, right = 0, len(patience_sort_list)-1
        while left<right:

            mid = (left+right)//2

            if left==right-1:
                if patience_sort_list[mid][-1]>=num:
                    return left
                else:
                    return right
            
            if patience_sort_list[mid][-1] == num:
                return mid
            if patience_sort_list[mid][-1] < num:
                left=mid+1
            else:
                right=mid

        return left
    

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        patience_sort_list = []
        for num in nums:
            ind = self.get_ind(num, patience_sort_list)
            if ind==len(patience_sort_list):
                patience_sort_list.append([])
            patience_sort_list[ind].append(num)
        #print(patience_sort_list)
        return len(patience_sort_list)