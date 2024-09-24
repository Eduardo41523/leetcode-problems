# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Solved: 24/09/2024
# Runtime Beats: 71.23%
# Memory Beats: 81.73%

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        temp = head
        while True:
            if temp.next == None:
                return head            
            elif (temp.val == temp.next.val):
                if temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                    return head
            else:
                temp = temp.next