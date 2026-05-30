# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        set_address = set()

        curr = head

        while curr!=None:
            if curr.next==None:
                return False
            else:
                if curr in set_address:
                    return True
                else:
                    set_address.add(curr)
                    curr = curr.next
                    
        return False

        