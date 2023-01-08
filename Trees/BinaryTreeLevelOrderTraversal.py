# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []


        node_queue = deque()
        level_order_traversal_list = []        
        node_queue.append([root, 1])

        while node_queue:
            cur_node, level = node_queue[0]
            node_queue.popleft()
            if level>len(level_order_traversal_list):
                level_order_traversal_list.append([])
            level_order_traversal_list[-1].append(cur_node.val)
            
            if cur_node.left:
                node_queue.append([cur_node.left, 1+level])
            
            if cur_node.right:
                node_queue.append([cur_node.right,1+level])

        return level_order_traversal_list