class Solution:
    def check_dicts(self, dict1, dict2):
        for key in dict1.keys():
            if dict2[key]!=dict1[key]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        s1_char_count_dict = {ch:0 for ch in "qwertyuiopasdfghjklzxcvbnm"}
        cur_window_char_count_dict = {ch:0 for ch in "qwertyuiopasdfghjklzxcvbnm"}
        
        for ch in s1:
            s1_char_count_dict[ch]+=1

        left, right = 0, 0
        while right-left+1<=len(s1):
            cur_window_char_count_dict[s2[right]]+=1
            right+=1
        
        if self.check_dicts(s1_char_count_dict, cur_window_char_count_dict):
            return True

        while right<len(s2):
            cur_window_char_count_dict[s2[right]]+=1
            cur_window_char_count_dict[s2[left]]-=1
            left+=1
            right+=1
            if self.check_dicts(s1_char_count_dict, cur_window_char_count_dict):
                return True
        return False