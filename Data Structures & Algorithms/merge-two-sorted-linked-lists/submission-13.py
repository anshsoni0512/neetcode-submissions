# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # node = ListNode()
        # dummy = node

        # while list1!= None and list2!= None: # if anyone false means anyone list is empty
        #     if list1.val<=list2.val:
        #         node.next = list1   # insert value
        #         list1 = list1.next  # move curr1 forward
            
        #     else:
        #         node.next = list2 
        #         list2 = list2.next

        #     node = node.next  # go to latest node after adding

        # # if anyone of the list is completed
        # if list1==None:
        #     node.next = list2
        # else:
        #     node.next = list1   # suppose list1 is empty then node.next is assigned to curr2 and curr2 is linked with "remaining" list2

        # return  dummy.next  # dummy is 1st element that is garbage so we want second element as our list starts from 2nd element so dummy.next





        node = ListNode()
        dummy = node    # dummy becomes head of the node as we have to return the first elment of the list so we define dummy as node v arianle will go to the last 

        c1 = list1
        c2 = list2
        while c1!=None and c2!=None:    # if any one list is empty exit this loop
            if c1.val<=c2.val:
                node.next = c1
                c1 = c1.next
            else:
                node.next = c2
                c2 = c2.next
            node = node.next   # update the node 

        if c1==None:
            node.next = c2
        else:
            node.next = c1
        
        return dummy.next
