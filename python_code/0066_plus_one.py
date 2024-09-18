# https://leetcode.com/problems/plus-one/description/

# Solved: 18/09/2024
# Runtime Beats: 88.67%
# Memory Beats: 66.26%

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Easy solution
        # x = "".join(str(digit) for digit in digits)
        # x = str(int(x)+1)
        # output = []
        # for n in x:
        #     output.append(int(n))
        # return output

        # Slightly more elaborate solution
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
    
        return digits