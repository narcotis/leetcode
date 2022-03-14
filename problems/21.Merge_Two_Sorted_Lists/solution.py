# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_head = ListNode(next= list1)
        list2_head = ListNode(next= list2)
        
        ans_head = ListNode()
        ans_idx = ans_head
        
        idx1 = list1_head
        idx2 = list2_head
        
        
        while idx1.next is not None or idx2.next is not None:
            if idx1.next is not None and idx2.next is not None:
                if idx1.next.val >= idx2.next.val:
                    ans_idx.next = ListNode(val = idx2.next.val)
                    ans_idx = ans_idx.next
                    idx2 = idx2.next
                else:
                    ans_idx.next = ListNode(val = idx1.next.val)
                    ans_idx = ans_idx.next
                    idx1 = idx1.next
            elif idx1.next is not None:
                ans_idx.next = ListNode(val = idx1.next.val)
                ans_idx = ans_idx.next
                idx1 = idx1.next
            elif idx2.next is not None:
                ans_idx.next = ListNode(val = idx2.next.val)
                ans_idx = ans_idx.next
                idx2 = idx2.next
        
                
        return ans_head.next
