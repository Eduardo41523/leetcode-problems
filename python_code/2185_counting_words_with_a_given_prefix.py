# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09

# Solved: 10/01/2024
# Runtime Beats: 100.00%
# Memory Beats: 9.54%

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if pref not in word:
                pass
            elif word[0:len(pref)] == pref:
                count += 1

        return count