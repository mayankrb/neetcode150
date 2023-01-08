"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur_node = head
        #insert new nodes
        while cur_node:
            aux_node = Node(cur_node.val, cur_node.next, None)
            cur_node.next = aux_node
            cur_node = aux_node.next
        
        #set random pointers
        orig_node, aux_node = head, head.next
        while aux_node:
            if orig_node.random:
                aux_node.random = orig_node.random.next 
            else:
                aux_node.random = None
            orig_node = aux_node.next
            if orig_node:
                aux_node = orig_node.next
            else:
                aux_node = None
                
        #return new list
        cur_node = head
        returning_head = head.next
        while cur_node:
            next_node = cur_node.next
            cur_node.next = next_node.next
            cur_node=cur_node.next
            if cur_node:
                next_node.next = cur_node.next
            else:
                next_node.next = None
            next_node = next_node.next
                
        return returning_head