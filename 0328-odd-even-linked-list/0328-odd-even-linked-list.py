# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  

        x = head
        y = head.next 
        h2 = y  

        while y and y.next:
            x.next = y.next  
            x = x.next  
            y.next = x.next  
            y = y.next  

        x.next = h2
        return head