# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

# Solved: 13/09/2024
# Runtime Beats: 62.71%
# Memory Beats: 83.05%

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                count += 1

        return count