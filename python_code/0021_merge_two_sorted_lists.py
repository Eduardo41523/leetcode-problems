# https://leetcode.com/problems/merge-two-sorted-lists/

# Solved: 22/09/2024
# Runtime Beats: 89.91%
# Memory Beats: 34.82%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Deal with cases in which one or both lists are empty
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        # Deal with all other cases
        new_list = None

        # Decide on which node to start
        # This node will be removed at the end
        if list1.val == list2.val or list1.val < list2.val:
            new_list = ListNode(list1.val)
        else:
            new_list = ListNode(list2.val)
        
        # Join and sort the linked lists in one go
        temp = new_list
        while(True):
            if(list1 == None and list2 == None):
                break
            elif(list2 == None):
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            elif(list1 == None):
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            elif(list1.val <= list2.val):
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            elif(list1.val > list2.val):
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        return new_list.next