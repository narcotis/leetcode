# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        c = ListNode()
        c_head = c
        carry = 0
        while a or b or carry:
            val1 = a.val if a else 0
            val2 = b.val if b else 0
            carry, val3 = divmod(val1 + val2 + carry, 10)
            
            c.next = ListNode(val3)
            c = c.next
            
            a = a.next if a else None
            b = b.next if b else None
        
        return c_head.next
                    
