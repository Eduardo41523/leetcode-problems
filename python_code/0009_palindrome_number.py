# https://leetcode.com/problems/palindrome-number/

# Solved: 15/09/2024
# Runtime Beats: 86.47%
# Memory Beats: 40.26%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]