# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        l = dummy
        r = dummy
        dummy.next = head

        while n>-1:
            r = r.next  # untill n becomes  we are adding one extra gap
            n=n-1
        
        # we have shifted the right pointer

        while r!=None:   # if r is not equal to none then move right and left pointers
            l=l.next   
            r=r.next
        l.next = l.next.next

        return dummy.next



        