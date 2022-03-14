# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        head = ListNode(next = head)
        idx = head
        tmp = idx

        
        while idx is not None:
            for i in range(n):
                tmp = tmp.next
                
            
            if tmp.next is None:
                if n == 1:
                    idx.next = None
                else:
                    idx.next = idx.next.next
                return head.next
            
            idx = idx.next
            tmp = idx
