class Solution:
    def combinationSumHelper(self, candidates, ans_set, cur_arr, remaining_sum):
        #print(remaining_sum, cur_arr)
        if remaining_sum<0:
            return 
        if remaining_sum == 0:
            ans_set.add(tuple(sorted(cur_arr)[:]))
            return
            
        for num in candidates:
            if num<=remaining_sum:
                cur_arr.append(num)
                self.combinationSumHelper(candidates, ans_set, cur_arr, remaining_sum-num)
                cur_arr.pop()
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations =set()
        self.combinationSumHelper(candidates, combinations, [], target)
        combinations  = [list(combination) for combination in combinations]
        return combinations