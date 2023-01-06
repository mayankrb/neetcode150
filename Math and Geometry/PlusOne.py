class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        flag = True
        answer = []
        while i < len(digits):
            if digits[len(digits)-1-i]!=9:
                flag = False
                break
            else:
                answer.append(0)
            i+=1
        if flag==False:
            answer.append(1+digits[len(digits)-1-i])
            i+=1        
            while i < len(digits):
                answer.append(digits[len(digits)-1-i])
                i+=1
        
        else:
            answer.append(1)
        return reversed(answer)