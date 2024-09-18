# https://leetcode.com/problems/sqrtx/description/

# Solved: 13/09/2024
# Runtime Beats: 46.90%
# Memory Beats: 19.45%

class Solution:
    def mySqrt(self, x: int) -> int:
        # Solution not allowed
        # return int(x**(1/2))

        # Imperfect solution
        for i in range(46341 + 1):
            if i*i > x:
                return i-1