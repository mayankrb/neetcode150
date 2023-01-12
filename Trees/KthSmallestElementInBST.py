# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, rank_and_num_arr, k):
        if node==None:
            return
        self.solve(node.left, rank_and_num_arr, k)
        rank, num = rank_and_num_arr
        if rank==k:
            return 
        else:
            rank_and_num_arr[:] = [rank+1, node.val]
        self.solve(node.right, rank_and_num_arr, k)
        return 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank_and_num_arr = [0, -1]
        self.solve(root, rank_and_num_arr, k)
        return rank_and_num_arr[1]