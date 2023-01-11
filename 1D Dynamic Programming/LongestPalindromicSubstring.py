class Solution:
    def move_around_center(self, left_center,right_center, s):
        count = 0
        if left_center == right_center:
            count = -1
        while left_center>=0 and right_center<len(s) and s[left_center]==s[right_center]:
            count+=2
            left_center-=1
            right_center+=1
        return count 
    def longestPalindrome(self, s: str) -> str:
        max_count = 1
        start_ind = 0
        for i in range(0, len(s)-1):
            count1 = self.move_around_center(i, i, s)
            count2 = self.move_around_center(i, i+1, s)
            if count1>max_count:
                ind = i-count1//2
                start_ind = ind
                max_count = count1
            if count2>max_count:
                ind = i+1 - count2//2
                start_ind = ind
                max_count = count2

        return s[start_ind:start_ind+max_count]