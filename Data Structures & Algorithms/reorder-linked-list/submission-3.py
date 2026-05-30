# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        left = head
        right = left.next


# we have to stop at last node so right.next is none then stop 
## Example:
# ```
# List: 1 → 2 → 3 → 4 → None
#                      ↑
#                    right

# - while right: ✓ (right is 4, exists)
# - Inside loop: right.next.next
#   - right.next = None
#   - None.next = ❌ CRASH!

        while right and right.next:  # dont let the right pointer go to null and finding middle value
            left = left.next
            right = right.next.next


#             Step 1: Find middle
# List: 1 → 2 → 3 → 4 → None
#            ↑
#           left (stops at 2)

# second = left.next  # second points to 3
# Step 2: Reverse second half
# After reversing:
# 4 → 3 → None
# ↑
# prev

# But node 2 still points to 3!
# 1 → 2 → 3 ← 4
#      ↑   ↑
#     left prev

# Step 1: Find middle and SPLIT
# 1 → 2 → None    (first half)
# 3 → 4 → None    (second half, before reverse)

# Step 2: Reverse
# 1 → 2 → None
# 4 → 3 → None    (after reverse)

# Step 3: Merge cleanly
# 1 → 4 → 2 → 3 → None  ✓ (no cycles!)



        second = left.next
        prev = None
        left.next = None  # ✓ Split the two halves
        # Why: Without this, the first half still connects to second half, causing infinite loops when merging.

        
        
        while second:    # reversing the list (2nd half)
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        # now merging the list
        first = head
        tail = prev    # here second is null after the reversing
        while tail:
            tmp1 = first.next
            tmp2 = tail.next
            first.next = tail
            tail.next = tmp1
            first = tmp1
            tail = tmp2
        
        
        