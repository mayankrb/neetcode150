from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        
        max_profit = 0
        right= 1
        min_ind = 0

        while right<len(prices):
            if prices[right]<=prices[min_ind]:
                min_ind = right
            else:
                max_profit = max(max_profit, prices[right]-prices[min_ind])
                
            right+=1
        return max_profit