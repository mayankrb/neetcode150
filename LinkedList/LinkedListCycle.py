# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None or head.next.next==None:
            return False
        slow_ptr, fast_ptr = head.next, head.next.next
        while slow_ptr!=fast_ptr :
            if slow_ptr == None or fast_ptr == None or slow_ptr.next==None or fast_ptr.next==None:
                return False
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return True
            