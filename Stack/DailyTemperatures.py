from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = deque()
        num_waiting_days = [0 for temp in temperatures]
        for cur_ind, cur_temp in enumerate(temperatures):
            if not temp_stack:
                temp_stack.append([cur_temp, cur_ind])
                continue
            if cur_temp>temp_stack[-1][0]:
                while temp_stack and cur_temp>temp_stack[-1][0]:
                    last_temp, last_ind = temp_stack[-1]
                    temp_stack.pop()
                    num_waiting_days[last_ind] = cur_ind-last_ind
            temp_stack.append([cur_temp, cur_ind])
        return num_waiting_days
        