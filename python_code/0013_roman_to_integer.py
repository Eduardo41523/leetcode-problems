# https://leetcode.com/problems/roman-to-integer/description/

# Solved: 16/09/2024
# Runtime Beats: 95.11%
# Memory Beats: 88.66%

class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0

        roman_characters = ["I", "V", "X", "L", "C", "D", "M", "", ""]

        for i, char in enumerate(s):
            for j in range(len(roman_characters)):
                if char == roman_characters[j]:
                    # Powers of 10
                    if j % 2 == 0:
                        if i < len(s)-1 and s[i+1] in roman_characters[j+1:j+3]:
                            n -= pow(10, j/2)
                        else:
                            n += pow(10, j/2)
                    # Powers of 10, over 2 
                    if j % 2 == 1:
                        n += 5 * pow(10, (j-1)/2)

                    break
                        
        return int(n)