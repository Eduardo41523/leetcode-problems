# https://leetcode.com/problems/add-two-numbers/description/

# Solved: 12/09/2024
# Runtime Beats: 5.46%
# Memory Beats: 74.75%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listnode_to_list(listnode):
            listnode_list = []
            while listnode.next != None:
                listnode_list.append(listnode.val)
                listnode = listnode.next
            listnode_list.append(listnode.val)

            return listnode_list
        
        def list_to_listnode(listnode_list):
            listnode = ListNode(listnode_list[-1], None)
            for i in range (len(listnode_list)-1):
                listnode = ListNode(listnode_list[-(i+2)], listnode)

            return listnode

        def listnode_list_to_reversed_int(listnode_list):
            reveresed_listnode_list = reversed(listnode_list)
            reversed_number = int(''.join(str(n) for n in reveresed_listnode_list))
            return reversed_number

        def int_reversed_and_to_list(integer):
            int_list = [int(digit) for digit in str(integer)]
            int_list.reverse()
            return int_list

        # Convert both listnodes to lists
        l1_as_list = listnode_to_list(l1)
        l2_as_list = listnode_to_list(l2)

        # Reverse and convert to integers
        first_number = listnode_list_to_reversed_int(l1_as_list)
        second_number = listnode_list_to_reversed_int(l2_as_list)

        # Add up integers
        two_numbers_added = first_number + second_number

        # Convert sum to reversed list and back to a nodelist
        result_reversed_list = int_reversed_and_to_list(two_numbers_added)
        result_listnode = list_to_listnode(result_reversed_list)

        return result_listnode