# https://leetcode.com/problems/length-of-last-word/description/

# Solved: 20/09/2024
# Runtime Beats: 52.78%
# Memory Beats: 10.64%

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                return length
        return length