# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #return diameter and max depth
    def solve(self, root):
        if root==None:
            return [0, 0]
        left_diameter, left_max_depth = self.solve(root.left)
        right_diameter, right_max_depth = self.solve(root.right)
        diameter = max([1+left_max_depth+right_max_depth, left_diameter, right_diameter])
        depth = 1 + max(left_max_depth, right_max_depth)
        return [diameter, depth]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, depth = self.solve(root)
        return diameter-1