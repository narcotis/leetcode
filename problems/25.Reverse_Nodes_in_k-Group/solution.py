# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        
        tmp = head
        idx1 = head
        idx2 = head
        
        while tmp.next is not None:
            
            tmp_list = []
            # start point
            idx1 = tmp
            for i in range(k):
                if tmp.next is not None:
                    tmp = tmp.next
                    tmp_list.append(tmp.val)
                else:
                    break
            # end point
            idx2 = tmp
            
            if len(tmp_list) == k:
                for val in reversed(tmp_list):
                    tmp = ListNode(val=val)
                    idx1.next = tmp
                    idx1 = idx1.next
                idx1.next = idx2.next
                tmp = idx1
            
        
        return head.next
