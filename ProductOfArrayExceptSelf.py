class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return nums[::-1]
        forward_pdt, backward_pdt = nums[:], nums[:]
        backward_pdt.append(1)
        answer_arr = []

        for ind in range(1, len(nums)):
            forward_pdt[ind]*=forward_pdt[ind-1]

        for ind in range(len(nums)-1, -1, -1):
            backward_pdt[ind]*=backward_pdt[ind+1]

        answer_arr.append(backward_pdt[1])
        for ind in range(1, len(forward_pdt)):
            answer_arr.append(forward_pdt[ind-1]*backward_pdt[ind+1])
        return answer_arr