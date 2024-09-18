# https://leetcode.com/problems/longest-common-prefix/description/

# Solved: 16/09/2024
# Runtime Beats: 68.14%
# Memory Beats: 71.28%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # lcp is short for longest common prefix
        lcp = strs[0]
        for string in strs: 
            for i in range(len(lcp)):
                if i > len(string)-1:
                    lcp = string
                    break
                elif lcp[i] != string[i]:
                    lcp = string[0:i]
                    break
            if lcp == "":
                break
        return lcp