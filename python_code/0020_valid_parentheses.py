# https://leetcode.com/problems/valid-parentheses/description/

# Solved: 18/09/2024
# Runtime Beats: 99.33%
# Memory Beats: 9.28%

class Solution:
    def isValid(self, s: str) -> bool:
        waiting_close = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                waiting_close.append(")")
            elif char == "[":
                waiting_close.append("]")
            elif char == "{":
                waiting_close.append("}")
            else:
                if len(waiting_close) > 0 and char == waiting_close[-1]:
                    waiting_close.pop()
                else:
                     return False
        if len(waiting_close) > 0:
            return False
        return True