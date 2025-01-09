# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

# Solved: 10/01/2025
# Runtime Beats: 89.31%
# Memory Beats: 6.48%

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return(str2.startswith(str1) and str2.endswith(str1))

        count = 0
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count