# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_list(self, head1, head2):
        while head2:
            temp = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = temp
        return head1
    def reverse_list(self, head):
        if head.next == None:
            return head
        previous, cur = None, head
        while cur:
            temp = cur.next
            cur.next = previous
            previous = cur
            cur = temp
        return previous

    def print_list(self, head):
        while head:
            print(head.val, end = " ")
            head = head.next
        print()

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        odd_len = True
        slow_ptr, fast_ptr = head, head
        while fast_ptr:
            if fast_ptr.next==None or fast_ptr.next.next==None:
                break
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        head2 = slow_ptr.next
        slow_ptr.next = None
        #print(head2)
        head2 = self.reverse_list(head2)
        #self.print_list(head)
        #self.print_list(head2)
        head = self.merge_two_list(head, head2)