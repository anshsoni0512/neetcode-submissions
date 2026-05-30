# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr != None:
            nxt = curr.next   # first assign nxt then break the forward link
            curr.next = prev   # pointing in reverse direction
            prev = curr
            curr = nxt
        return prev