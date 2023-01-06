class Solution:
    def solve(self, ans_arr, cur_parenthesis, forward_remaining, backward_remaining):
        if forward_remaining==0 and backward_remaining==0:
            ans_arr.add("".join(cur_parenthesis))
            return
        if backward_remaining>forward_remaining:
            cur_parenthesis.append(")")
            self.solve(ans_arr, cur_parenthesis, forward_remaining, backward_remaining-1)
            cur_parenthesis.pop()
        if forward_remaining>0:
            cur_parenthesis.append("(")
            self.solve(ans_arr, cur_parenthesis, forward_remaining-1, backward_remaining)
            cur_parenthesis.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        cur_parenthesis = []
        ans_arr = set()
        self.solve(ans_arr, cur_parenthesis, n, n)
        ans_arr = list(ans_arr)
        return ans_arr