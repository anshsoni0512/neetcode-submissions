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
        #             curr = curr.next   # now go to next element
                    
        # return False


    
        s = head
        f = head
        while f!= None and f.next!=None:  # use 'and' because all the condttions should be satisfied not any one of them 

            s = s.next        # move s 1 step
            f = f.next.next   # move f 2 steps     None.next gives error thats why we check in while loop condition
            if s==f:        # if they are at same postion means there is cycle
                return True
            else:
                continue
                
        return False

        