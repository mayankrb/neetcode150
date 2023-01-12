# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def get_preorder(self, root, preorder):
        if root==None:
            return preorder.append("None")
        #print(root.val)
        preorder.append(str(root.val))
        self.get_preorder(root.left, preorder)
        self.get_preorder(root.right, preorder)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ["None"]
        self.get_preorder(root, s)
        return ".".join(s)
    
    def dfs(self, nodes, ind):
        if ind[0]>=len(nodes) or nodes[ind[0]]=="None":
            ind[0]+=1
            return None
        root = TreeNode(int(nodes[ind[0]]))
        ind[0]+=1
        root.left = self.dfs(nodes, ind)
        root.right = self.dfs(nodes, ind)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(".")
        root = self.dfs(nodes, [1])
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))