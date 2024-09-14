# https://leetcode.com/problems/zigzag-conversion/description/

# Solved: 13/09/2024
# Runtime Beats: 54.00%
# Memory Beats: 60.07%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Create rows for the characters
        lists = []
        for i in range(numRows):
            lists.append([])
        
        # Put characters into rows
        direction = 1
        current_list = 0
        for i in range(len(s)):
            lists[current_list].append(s[i])

            if numRows != 1:
                current_list += direction
                if (i + 1) % (numRows - 1) == 0:
                    direction *= -1
        
        # Combine rows into resulting string
        result = ""
        for list_element in lists:
            list_element_string = "".join(list_element)
            result += list_element_string

        return result
