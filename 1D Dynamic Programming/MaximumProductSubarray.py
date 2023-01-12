class Solution:
    def kadane(self, nums):
        max_pdt = max(nums)
        cur_pdt = 1
        for i, num in enumerate(nums):
            if num==0:
                cur_pdt = 1
                continue
            cur_pdt *= num
            max_pdt = max(max_pdt, cur_pdt)
        return max_pdt

    def maxProduct(self, nums: List[int]) -> int:
        max_pdt_forward = self.kadane(nums)
        max_pdt_backward = self.kadane(nums[::-1])
        max_pdt = max(max_pdt_backward, max_pdt_forward)
        return max_pdt