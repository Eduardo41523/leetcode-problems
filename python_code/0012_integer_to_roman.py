# https://leetcode.com/problems/integer-to-roman/description/

# Solved: 16/09/2024
# Runtime Beats: 62.32%
# Memory Beats: 57.14%

class Solution:
    def intToRoman(self, num: int) -> str:
        def digitToRoman(char, unit, five, ten):
            if char in "0":
                output = ""
            if char in "123":
                output = unit * int(char)
            elif char in "4":
                output = unit + five
            elif char in "5":
                output = five
            elif char in "678":
                output = five + unit * (int(char)-5)
            elif char in "9":
                output = unit + ten
            return output

        output = []
        num = str(num)
        for i in range(1, len(num)+1):
            char = num[-i]
            if i == 1:
                output.append(digitToRoman(char, "I", "V", "X"))
            if i == 2:
                output.append(digitToRoman(char, "X", "L", "C"))
            if i == 3:
                output.append(digitToRoman(char, "C", "D", "M"))
            if i == 4:
                # The constraints of the problem make it so that "?" will never occur
                output.append(digitToRoman(char, "M", "?", "?"))
        output = output[::-1]
        output = "".join(output)

        return output
