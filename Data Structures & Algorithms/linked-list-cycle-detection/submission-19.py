# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # there could be duplicate vlaues so we dont save values we save nodes


        # set_address = set()

        # curr = head

        # while curr!=None:
        #     if curr.next==None:  # if it is a last node then we never get cur.next = None
        #         return False
        #     else:
        #         if curr in set_address:  # if the curr address in present inside set then we have already visited it
        #             return True
        #         else:
        #             set_address.add(curr)  # if the curr address is not in set we will add in the set
        #             curr = curr.next
                    
        # return False


    
        s = head
        f = head
        while s!= None and f!= None and f.next!=None:

            s = s.next        # move s one step
            f = f.next.next   # move f 2 steps
            if s==f:        # if they are at same postion means there is cycle
                return True
            else:
                continue
                
        return False

        