class Solution:
    def isHappy(self, n: int) -> bool:
        visited_dict = {n:1}
        while True:
            cur_sum = 0
            while n:
                digit = n%10
                cur_sum+=digit**2
                n = n//10
            n = cur_sum
            if n==1:
                return True
            if n in visited_dict.keys():
                return False
            visited_dict[n]=1
        