import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, (-stone, stone))
        while len(max_heap)>1:
            larger_stone = max_heap[0][1]
            heapq.heappop(max_heap)
            smaller_stone = max_heap[0][1]
            heapq.heappop(max_heap)
            if larger_stone-smaller_stone>0:
                heapq.heappush(max_heap, (smaller_stone-larger_stone, larger_stone-smaller_stone))
        if not max_heap:
            return 0
        return max_heap[0][1]