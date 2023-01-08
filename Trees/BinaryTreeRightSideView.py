# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, cur_level, ans_list):
        if root==None:
            return 
        if cur_level>len(ans_list):
            ans_list.append(root.val)
        self.solve(root.right, cur_level+1, ans_list)
        self.solve(root.left, cur_level+1, ans_list)
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans_list = []
        self.solve(root, 1, ans_list)
        return ans_list