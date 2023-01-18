from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = deque()
        stack.append([0, -1])
        #fill the the stack
        for cur_ind, cur_height in enumerate(heights):
            #print(stack, max_area)
            while len(stack)>1 and stack[-1][0]>cur_height:
                top_height, top_ind = stack[-1]
                stack.pop()
                width = cur_ind-stack[-1][1]-1
                max_area = max(max_area, width*top_height)
            stack.append([cur_height, cur_ind])

        #if we have elements in stack remaining
        if stack:
            while len(stack)>1:
                #print(stack)
                top_height, top_ind = stack[-1]
                stack.pop()
                width = len(heights)-stack[-1][1]-1
                #print(width, top_height)
                max_area = max(max_area, width*top_height)
        return max_area