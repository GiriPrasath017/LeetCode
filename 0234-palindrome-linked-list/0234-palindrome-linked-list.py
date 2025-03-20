# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = ListNode(0)
        x.next = head
        c = x
        xl = []
        while c.next:
            xl.append(c.next.val)
            c = c.next
        
        return xl == xl[::-1] 