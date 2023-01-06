class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_dict = {}
        are_valid_anagrams = True
        
        for ch in s:
            try:
                count_dict[ch]+=1
            except:
                count_dict[ch]=1
        
        for ch in t:
            try:
                count_dict[ch]-=1
            except:
                are_valid_anagrams = False
                break
        
        for ch, val in count_dict.items():
            if val!=0:
                are_valid_anagrams=False
                break
        return are_valid_anagrams