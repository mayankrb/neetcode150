class Solution:
    def get_sorted_tuple(self, nums):
        nums_tuple = tuple(sorted(nums))
        return nums_tuple
    
    def get_list_valid_combinations(self, nums, valid_combinations_set):
        ans = []
        for cur_combination in valid_combinations_set:
            cur_combination_list = [num for num in cur_combination]
            ans.append(cur_combination_list)
        return ans

    def combinationSum2Helper(self, candidates, valid_combinations_set, cur_combination, remaining_target, cur_ind):
        if remaining_target<0 or cur_ind>len(candidates):
            return
        if remaining_target==0:
            valid_combinations_set.add(self.get_sorted_tuple(cur_combination))
            return
        if sum(candidates[cur_ind+1:])>=remaining_target:
            self.combinationSum2Helper(candidates, valid_combinations_set, cur_combination, remaining_target, cur_ind+1)
        if cur_ind < len(candidates) and candidates[cur_ind]<=remaining_target:
            cur_combination.append(candidates[cur_ind])
            self.combinationSum2Helper(candidates, valid_combinations_set, cur_combination, remaining_target-candidates[cur_ind], cur_ind+1)
            cur_combination.pop()
        return
            
    def get_modified_candidates(self, candidates, target):
        count_dict = {num:0 for num in candidates}
        for num in candidates:
            count_dict[num]+=1
            count_dict[num] = min(target//num+1, count_dict[num])
        candidates = []
        for key, val in count_dict.items():
            candidates = candidates + [key]*val
        return candidates


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        modified_candidates = self.get_modified_candidates(candidates, target)
        valid_combinations_set = set()
        cur_combination = []
        cur_ind = 0
        self.combinationSum2Helper(modified_candidates, valid_combinations_set, cur_combination, target, 0)
        return self.get_list_valid_combinations(modified_candidates, valid_combinations_set)