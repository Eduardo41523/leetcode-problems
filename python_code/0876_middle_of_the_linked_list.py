# https://leetcode.com/problems/middle-of-the-linked-list/description/
# This problem was also featured in the Udemy Course "Python Data Structures & Algorithms + LEETCODE Exercises"

# Solved: 21/09/2024
# Runtime Beats: 88.92%
# Memory Beats: 11.35%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = head
        slow_pointer = head
        while fast_pointer.next:
            if fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            else:
                slow_pointer = slow_pointer.next
                break
            
        return slow_pointer
        