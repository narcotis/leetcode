# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(next=head)
        tmp = head
        idx1 = head
        idx2 = head
        
        while tmp.next is not None and tmp.next.next is not None:
            idx1 = tmp.next
            idx2 = tmp.next.next
            
            tmp.next = idx2
            idx1.next = idx2.next
            idx2.next = idx1
            
            tmp = tmp.next.next
        
        return head.next
