class Solution:
    def check_all_empty(self, char_set, count_dict):
        for char in char_set:
            if count_dict[char]>0:
                return False
        return True

    def partitionLabels(self, s: str) -> List[int]:
        count_dict = {}
        for ch in s:
            try:
                count_dict[ch]+=1
            except:
                count_dict[ch]=1
        ans_count_arr = []
        cur_ind = 0
        cur_char_set = set()
        cur_count = 0
        while cur_ind<len(s):
            cur_char = s[cur_ind] 
            cur_char_set.add(cur_char)
            count_dict[cur_char]-=1
            cur_count+=1
            if self.check_all_empty(cur_char_set, count_dict):
                ans_count_arr.append(cur_count)
                cur_count = 0
                cur_char_set.clear()
            cur_ind+=1
        if cur_count>0:
            ans_count_arr.append(cur_count)
        return ans_count_arr