# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Solved: 23/09/2024
# Runtime Beats: 54.60%
# Memory Beats: 23.68%

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if "".join(haystack[i:i+len(needle)]) == needle:
                return i
        return -1