class Solution:
    def solve_dp(self, dp_dict, coins, amount):
        if amount<0:
            return -1
        if amount in dp_dict.keys():
            return dp_dict[amount]
        
        min_ans = 10000000

        for coin in coins:
            if coin<=amount:
                ans = 1+self.solve_dp(dp_dict, coins, amount-coin)
                if ans>0:
                    min_ans = min(ans, min_ans)
        dp_dict[amount]=min_ans
        return dp_dict[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_dict = {coin:1 for coin in coins}
        dp_dict[0] = 0
        dp_dict[amount] = self.solve_dp(dp_dict, coins, amount)
        #print(dp_dict)
        if dp_dict[amount]==10000000:
            return -1
        return dp_dict[amount]