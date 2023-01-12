# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve_goodness(self, root, max_val, count_arr):
        if root==None:
            return
        if root.val>=max_val:
            count_arr[0]+=1
        max_val = max(max_val, root.val)
        self.solve_goodness(root.left, max_val, count_arr)
        self.solve_goodness(root.right, max_val, count_arr)
        return


    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count_arr = [0]
        self.solve_goodness(root, root.val, count_arr)
        return count_arr[0]