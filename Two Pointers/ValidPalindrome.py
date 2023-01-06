class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ind, right_ind = 0, len(s)-1
        s = s.lower()
        while left_ind<right_ind:
            if not s[left_ind].isalnum():
                left_ind+=1
                continue
            if not s[right_ind].isalnum():
                right_ind-=1
                continue
                
            if s[left_ind]!=s[right_ind]:
                return False
            left_ind+=1
            right_ind-=1
        return True