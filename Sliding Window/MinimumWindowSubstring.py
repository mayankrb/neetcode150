class Solution:
    def check_if_possible(self, cur_count_dict, target_count_dict):
        for key in target_count_dict.keys():
            if key not in cur_count_dict.keys() or cur_count_dict[key]<target_count_dict[key]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        target_count_dict = {}
        cur_count_dict = {}
        min_window_left, min_window_right = -1, -1
        left, right = 0, 0
        for ch in t:
            try:
                target_count_dict[ch]+=1
            except:
                target_count_dict[ch]=1
        
        print(target_count_dict)

        while right<len(s):
            try:
                cur_count_dict[s[right]]+=1
            except:
                cur_count_dict[s[right]]=1
            #print(cur_count_dict)
            while self.check_if_possible(cur_count_dict, target_count_dict) and left<=right:
                if right-left<min_window_right-min_window_left or min_window_left==-1 or min_window_right==-1:
                    min_window_left, min_window_right = left, right
                cur_count_dict[s[left]]-=1
                left+=1
            right+=1
        return s[min_window_left:min_window_right+1]
