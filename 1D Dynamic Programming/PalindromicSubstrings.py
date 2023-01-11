class Solution:
    def move_around_center(self, left_center,right_center, s):
        count = 0
        while left_center>=0 and right_center<len(s) and s[left_center]==s[right_center]:
            count+=1
            left_center-=1
            right_center+=1
        return count 
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        start_ind = 0
        s = s + "*" 
        for i in range(0, len(s)-1):
            count1 = self.move_around_center(i, i, s)
            count2 = self.move_around_center(i, i+1, s)
        
            total_count+=count1+count2

        return total_count

    