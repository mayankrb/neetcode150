import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        ans = []
        for point in points:
            x, y = point
            dist = x**2 + y**2
            print(x, y, dist)
            heapq.heappush(closest_points, (-dist, point))
            if len(closest_points)>k:
                heapq.heappop(closest_points)

        while closest_points:
            _, point = closest_points[0]
            heapq.heappop(closest_points)
            ans.append(point)
        return ans