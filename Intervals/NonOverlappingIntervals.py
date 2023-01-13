class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        num_interval_to_erase_forward = 0
        cur_start, cur_end = intervals[0]
        for ind in range(1, len(intervals)):
            if intervals[ind][0]<cur_end:
                num_interval_to_erase_forward+=1
            else:
                cur_start, cur_end = intervals[ind]
        
        intervals.reverse()
        num_interval_to_erase_backward = 0
        cur_start, cur_end = intervals[0]
        for ind in range(1, len(intervals)):
            if intervals[ind][1]>cur_start:
                num_interval_to_erase_backward+=1
            else:
                cur_start, cur_end = intervals[ind]
        
        return min(num_interval_to_erase_forward, num_interval_to_erase_backward)