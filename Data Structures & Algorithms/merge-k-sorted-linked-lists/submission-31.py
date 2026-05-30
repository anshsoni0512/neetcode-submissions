# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

       

    #     if len(lists)==0:
    #         return None

        
    #     while len(lists)>1:
    #         mergedList = []
    #         for i in range(0,len(lists),2):
    #             #lists[0] and lists[1]
    #             l1 = lists[i]
               
    #             if (i+1) < len(lists):
    #                 l2=lists[i+1]
    #             else:
    #                 l2 = None
                
    #             mergedList.append(self.mergeList(l1,l2))
    #         lists = mergedList
    #     return lists[0]

    # def mergeList(self,l1,l2):
    #     dummy = ListNode()
    #     curr  = dummy
    #     while l1 != None and l2 != None:
    #         if l1.val<=l2.val:
    #             curr.next = l1
    #             l1= l1.next
    #         else:
    #             curr.next = l2
    #             l2 = l2.next
    #         curr = curr.next


    #     if l2==None:
    #         curr.next = l1
    #     else:
    #         curr.next = l2
    #     return dummy.next








        # If all lists were None, return None
        if not lists or len(lists) == 0:
            return None


        

        while len(lists)>1:
            mergedList = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if i+1<len(lists):    # index put of bound problem
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergedList.append(self.mergelists(l1,l2))
            lists = mergedList
        return lists[0]

    def mergelists(self, l1, l2):

        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1==None:
            node.next = l2
        else:
            node.next = l1
            
        return dummy.next

            


            

        