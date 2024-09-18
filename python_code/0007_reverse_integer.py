# https://leetcode.com/problems/reverse-integer/description/

# Solved: 13/09/2024
# Runtime Beats: 59.44%
# Memory Beats: 80.03%

class Solution:
    def reverse(self, x: int) -> int:
        # take note of the number's sign and make it positive 
        positive = True
        if x <= 0:
            positive = False
            x = x * -1
        
        # to string, reverse, and back to integer
        x = str(x)
        x = x[::-1]
        x = int(x)

        # change back to negative if necessary
        if not positive:
            x *= -1

        # deal with specified range
        if (x < pow(-2, 31) or x > pow(2, 31)-1):
            return 0

        return(x)