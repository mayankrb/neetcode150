class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        #find rank and partition based on count
        def find_rank(arr, k, start_ind, end_ind):
            pivot_ind = (start_ind+end_ind)//2
            cur_start_ind, cur_end_ind = start_ind, end_ind
            while cur_start_ind < pivot_ind:
                if arr[cur_start_ind][0] < arr[pivot_ind][0]:
                    arr[pivot_ind-1], arr[cur_start_ind] = arr[cur_start_ind], arr[pivot_ind-1]
                    arr[pivot_ind], arr[pivot_ind-1] = arr[pivot_ind-1], arr[pivot_ind] 
                    pivot_ind -= 1
                else:
                    cur_start_ind+=1
            while cur_end_ind > pivot_ind:
                if arr[cur_end_ind][0] >= arr[pivot_ind][0]:
                    arr[pivot_ind+1], arr[cur_end_ind] = arr[cur_end_ind], arr[pivot_ind+1]
                    arr[pivot_ind], arr[pivot_ind+1] = arr[pivot_ind+1], arr[pivot_ind] 
                    pivot_ind+=1
                else:
                    cur_end_ind-=1
            if pivot_ind-start_ind==k-1:
                return 
            if pivot_ind-start_ind>k-1:
                find_rank(arr, k, start_ind, pivot_ind-1)
            else:
                find_rank(arr, k-pivot_ind+start_ind-1, pivot_ind+1, end_ind)

        """
        Can be done in O(nlogn) by sorting or O(nlogk) by using a heap of size k
        But we can do this in O(n) by using rank finding algorithm
        """
        count_dict = {}
        ranked_arr = []
        top_k_frequent_elements = [] 
        for num in nums:
            try:
                count_dict[num]+=1
            except:
                count_dict[num]=1
        for num, count in count_dict.items():
            ranked_arr.append([count, num])
        #print(ranked_arr)
        #partition based on rank
        find_rank(ranked_arr, k, 0, len(ranked_arr)-1)        
        #print(ranked_arr)
        for i in range(k):
            top_k_frequent_elements.append(ranked_arr[i][1])
        
        return top_k_frequent_elements