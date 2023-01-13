class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        cur_start, cur_end = intervals[0]
        for ind in range(1, len(intervals)):
            if intervals[ind][0]<cur_end:
                return False
            else:
                cur_start, cur_end = intervals[ind]
        return True