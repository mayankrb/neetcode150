"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def dfs(self, node, node_dict, visited_dict):
        if node==None:
            return
        visited_dict[node] = True
        if node not in node_dict:
            node_dict[node] = Node(node.val, [])
        aux_node = node_dict[node]
        for neighbor in node.neighbors:
            if neighbor not in node_dict.keys():
                node_dict[neighbor] = Node(neighbor.val, [])
            aux_node.neighbors.append(node_dict[neighbor])
            if neighbor in visited_dict.keys():
                continue
            self.dfs(neighbor, node_dict, visited_dict)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        node_dict = {}
        visited_dict = {}
        self.dfs(node, node_dict, visited_dict)

        

        return node_dict[node]
