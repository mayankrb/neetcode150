# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        #smaller and larger
        final_head = list1
        
        if list2.val < list1.val:
            final_head = list2
            list2, list1 = list1, list2
        
        previous_node, cur_node = list1, list1.next
        while cur_node and list2:
            if cur_node.val>=list2.val:
                list2_new = list2.next
                previous_node.next = list2
                list2.next = cur_node
                previous_node = list2
                list2 = list2_new
            else:
                previous_node = cur_node
                cur_node = cur_node.next

        if list2:
            previous_node.next = list2

        return final_head