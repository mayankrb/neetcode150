class Solution: 
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #set smaller array to smaller_arr
        smaller_arr, larger_arr = nums1, nums2
        if len(larger_arr)<len(smaller_arr):
            smaller_arr, larger_arr = larger_arr, smaller_arr
        
        #store lengths
        total_len = len(smaller_arr)+len(larger_arr)
        half = (len(smaller_arr)+len(larger_arr))//2
        median = -1
        #s_left_ind, s_right_ind = indices of smaller arr
        s_left_ind, s_right_ind = 0, len(smaller_arr)-1
    
        
        #run binary search on smaller_arr
        while True:
            #candidate index in smaller_arr
            s_mid_ind = (s_left_ind+s_right_ind)//2   
            #find corresponding index in larger arr = half - number of elements from smaller array - 1(offset)
            l_ind = half-(s_mid_ind+1)-1   

            #candidates for median values
            s_left_candidate, s_right_candidate = float("-inf"), float("inf")
            l_left_candidate, l_right_candidate = float("-inf"), float("inf")
            
            #take care of corner cases
            if s_mid_ind>=0:
                s_left_candidate = smaller_arr[s_mid_ind]
            if s_mid_ind+1<len(smaller_arr):
                s_right_candidate = smaller_arr[s_mid_ind+1]
            if l_ind>=0:
                l_left_candidate = larger_arr[l_ind]
            if l_ind+1<len(larger_arr):
                l_right_candidate = larger_arr[l_ind+1]
        
            candidates = [s_left_candidate, l_left_candidate, s_right_candidate, l_right_candidate]
            #if we found the median division correctly
            if s_left_candidate<=l_right_candidate and l_left_candidate <= s_right_candidate:
                #print(s_left_candidate, s_right_candidate, l_left_candidate, l_right_candidate)
                median = min(s_right_candidate, l_right_candidate)
                if total_len%2==0:
                    median += max(s_left_candidate, l_left_candidate)
                    median/=2
                break

            if s_left_candidate > l_right_candidate:
                s_right_ind = s_mid_ind-1
            else:
                s_left_ind = s_mid_ind+1
        
        return median
        
            


