class Solution:
    def solve(self, dp_dict, s, ind):
        if ind==len(s): 
            return 1
        if s[ind]=="0":
            return 0
        if ind in dp_dict.keys():
            return dp_dict[ind]
        if ind == len(s)-1:
            dp_dict[ind]=1
            return dp_dict[ind]
        dp_dict[ind] = self.solve(dp_dict, s, ind+1)
        if s[ind] == "1" or (s[ind]=="2" and s[ind+1] in "0123456"):
            dp_dict[ind] += self.solve(dp_dict, s, ind+2)
        return dp_dict[ind]
        
    def numDecodings(self, s: str) -> int:
        dp_dict = {}
        dp_dict[0] = self.solve(dp_dict, s, 0)
        return dp_dict[0]