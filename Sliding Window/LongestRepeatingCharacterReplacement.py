class Solution:
    def check_if_not_valid(self, count_dict, k, cur_window_size):
        flag = True
        for ch in "QWERTYUIOPASDFGHJKLZXCVBNM":
            if cur_window_size - count_dict[ch] <= k:
                flag = False
        return flag

    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count_dict = {ch:0 for ch in "QWERTYUIOPASDFGHJKLZXCVBNM"}
        cur_window_size = 0
        max_window_size = 0
        while right < len(s):
            count_dict[s[right]]+=1
            cur_window_size += 1
            while left<=right and self.check_if_not_valid(count_dict, k, cur_window_size):
                count_dict[s[left]]-=1
                left+=1
                cur_window_size-=1
            #print(cur_window_size, max_window_size)
            max_window_size = max(max_window_size, cur_window_size)
            right+=1
        return max_window_size
        