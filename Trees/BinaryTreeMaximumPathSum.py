# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, cur_node, max_neg_val):
        if cur_node==None:
            #max_path including this node, max_path that does not include this node, max_path that just goes down including this node
            return [0, 0, 0]
        left_values = self.solve(cur_node.left, max_neg_val)
        right_values = self.solve(cur_node.right, max_neg_val)
        max_neg_val[0] = max(max_neg_val[0], cur_node.val)
        max_path_down_only = cur_node.val+max(left_values[-1], right_values[-1], 0)
        max_path_with_this_node = cur_node.val+max(0, left_values[-1]) + max(0,right_values[-1])
        max_path_without_this_node = max(max(left_values), max(right_values))
        return [max_path_with_this_node, max_path_without_this_node, max_path_down_only]

        
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_neg_val = [root.val]
        candidate =  max(self.solve(root, max_neg_val))
        if max_neg_val[0]<0:
            return max_neg_val[0]
        return candidate
        