# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        forward_ptr = head
        for i in range(n):
            forward_ptr = forward_ptr.next
        previous, cur = None, head
        while forward_ptr:
            previous = cur
            cur=cur.next
            forward_ptr = forward_ptr.next
        if not previous:
            return head.next
        else:
            previous.next = previous.next.next
        return head
        
            