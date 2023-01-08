# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return True, 0
        is_left_subtree_valid, left_height = self.solve(root.left)
        is_right_subtree_valid, right_height = self.solve(root.right)
        if not is_left_subtree_valid or not is_right_subtree_valid or abs(left_height-right_height)>1:
            return False, -1
        else:
            return True, 1+max(left_height, right_height)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, max_depth = self.solve(root)
        return is_balanced