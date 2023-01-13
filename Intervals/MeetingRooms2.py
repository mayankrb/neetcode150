import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return True
        min_heap = []
        intervals.sort()
        min_rooms = -1
        for interval in intervals:
            start, end = interval
            while min_heap and min_heap[0][1][1]<=start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, (end, (start, end)))
            min_rooms = max(min_rooms, len(min_heap))
        return min_rooms
        