# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        
        # append all the values of the nodes to the list
        for nodes in lists:
            while nodes:
                values.append(nodes.val)
                nodes = nodes.next
        
        values.sort()

                
        head = ListNode()
        idx = head
        
        for val in values:
            idx.next = ListNode(val = val)
            idx = idx.next
        
        return head.next
