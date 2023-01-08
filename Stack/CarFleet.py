from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_stats = [[position[i], speed[i]] for i in range(len(position))]
        combined_stats.sort()
        combined_stats.reverse()
        cur_ind = 1
        fleet_count = 1
        stack = deque()
        time_taken = [(target-combined_stats[i][0])/combined_stats[i][1] for i in range(len(combined_stats))]
        #print(combined_stats)
        #print(time_taken)

        stack.append(time_taken[0])

        for i in range(1, len(time_taken)):
            if time_taken[i] > stack[-1]:
                stack.pop()
                stack.append(time_taken[i])
                fleet_count+=1
            

        
        return fleet_count