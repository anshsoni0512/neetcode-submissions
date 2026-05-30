# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        node = ListNode()
        dummy = node

        while list1!= None and list2!= None: # if anyone false means anyone list is empty
            if list1.val<=list2.val:
                node.next = list1   # insert value
                list1 = list1.next  # move curr1 forward
            
            else:
                node.next = list2 
                list2 = list2.next

            node = node.next  # go to latest node after adding

        # if anyone of the list is completed
        if list1==None:
            node.next = list2
        else:
            node.next = list1   # suppose list1 is empty then node.next is assigned to curr2 and curr2 is linked with "remaining" list2

        return  dummy.next  # dummy is 1st element that is garbage so we want second element as our list starts from 2nd element so dummy.next