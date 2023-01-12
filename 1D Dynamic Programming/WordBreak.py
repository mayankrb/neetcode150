class Solution:
    def solve(self, s, start_ind, word_dict, dp_dict):
        if start_ind==len(s):
            return True
        if s[start_ind:] in word_dict.keys():
            return True
        if start_ind in dp_dict.keys():
            return dp_dict[start_ind]

        for i in range(start_ind, len(s)):
            if s[start_ind:i+1] in word_dict.keys() and self.solve(s, i+1, word_dict, dp_dict):
                dp_dict[start_ind]= True
                return True
        dp_dict[start_ind] = False
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = {word:1 for word in wordDict}
        
        if self.solve(s, 0, word_dict, {}):
            return True
        return False