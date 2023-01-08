# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #head of final linked list and priority queue
        returning_head, cur_node = None, None
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, [lists[i].val, i])

        heapq.heapify(pq)
        while pq:
            priority, ind = pq[0]
            heapq.heappop(pq)
            #print(priority, ind)
            
            top_node = lists[ind]
            lists[ind] = lists[ind].next
            
            if not returning_head:
                returning_head = top_node
                cur_node = top_node
            else:
                cur_node.next = top_node
                cur_node = cur_node.next
            if lists[ind]:
               heapq.heappush(pq, [lists[ind].val,  ind])

        return returning_head