class Solution:
    def check_valid(self, s):
        count = 0
        star_count = 0
        opening_bracket_count = 0
        closed_bracket_count = 0
        for ch in s:
            if ch=="*":
                star_count+=1
            elif ch=="(":
                opening_bracket_count+=1
            else:
                closed_bracket_count+=1
            if opening_bracket_count+star_count<closed_bracket_count:
                return False
        return True
        
    def checkValidString(self, s: str) -> bool:
        reverse_char_map = {"(":")", "*":"*", ")":"("}
        reverse_s = "".join([reverse_char_map[ch] for ch in s[::-1]])
        print(reverse_s)
        return self.check_valid(s) and self.check_valid(reverse_s)