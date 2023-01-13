class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        cur_interval_start, cur_interval_end = intervals[0]
        ind = 0
        while ind < len(intervals):
            if cur_interval_end>=intervals[ind][0]:
                cur_interval_end = max(intervals[ind][1], cur_interval_end)
                cur_interaval_start = min(intervals[ind][0], cur_interval_start)
                ind+=1
            else:
                merged_intervals.append([cur_interval_start, cur_interval_end])
                cur_interval_start, cur_interval_end = intervals[ind]
        
        merged_intervals.append([cur_interval_start, cur_interval_end])
        return merged_intervals