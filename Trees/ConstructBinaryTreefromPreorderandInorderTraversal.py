# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if 0==len(preorder) or 0==len(inorder):
            return None
        ind = 0
        root = TreeNode(preorder[0])
        while inorder[ind]!=preorder[0]:
            ind+=1
        root.left = self.buildTree(preorder[1:ind+1], inorder[0:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return root
                