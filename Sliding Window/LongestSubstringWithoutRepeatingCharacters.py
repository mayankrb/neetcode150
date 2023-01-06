class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        cur_len = 0
        s_dict = {}
        while right<len(s):
            try:
                if s_dict[s[right]]==1:
                    max_len =max(max_len, right-left)
                    while s[left]!=s[right]:
                        s_dict[s[left]]-=1
                        left+=1
                    left+=1
                else:
                    max_len = max(max_len, right-left+1)
                    s_dict[s[right]]=1
                right+=1
            except:
                s_dict[s[right]]=1
                max_len = max(max_len, right-left+1)
                right+=1
        return max_len